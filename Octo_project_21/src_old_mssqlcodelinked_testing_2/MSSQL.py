"""
MSSQL Database Initialization Module for OctoPreciGo
Supports both Network Authentication (Windows) and Cloud Authentication (SQL Server)
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class ProbeBasedIds(Base):
    """
    Table for storing probe-based identification settings
    """
    __tablename__ = 'ProbeBasedIds'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    UniqueSettings = Column(String(500), nullable=True)
    # Full settings fields to match CSV
    ProgramId = Column(Integer, nullable=True)
    ProgramName = Column(String(100), nullable=True)
    Dimension = Column(String(10), nullable=True)
    Formula = Column(String(50), nullable=True)
    MasterType = Column(String(50), nullable=True)
    MasterLower = Column(Float, nullable=True)
    Master = Column(Float, nullable=True)
    MasterHigher = Column(Float, nullable=True)
    UpperSpecificationLimit = Column(Float, nullable=True)
    UpperControlLimit = Column(Float, nullable=True)
    NominalValue = Column(Float, nullable=True)
    LowerControlLimit = Column(Float, nullable=True)
    LowerSpecificationLimit = Column(Float, nullable=True)
    Ovality = Column(String(10), nullable=True)
    Range = Column(Float, nullable=True)
    Method = Column(String(20), nullable=True)
    Case = Column(String(20), nullable=True)
    CaseT = Column(Float, nullable=True)
    LeastCount = Column(Float, nullable=True)
    ProbeSensitivity = Column(Integer, nullable=True)
    AirSensitivityQuotient = Column(Float, nullable=True)
    Channel = Column(Integer, nullable=True)
    created_date = Column(String(50), nullable=True)


class AOCBasedIds(Base):
    """
    Table for storing AOC-based identification settings
    """
    __tablename__ = 'AOCBasedIds'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    UniqueSettings = Column(String(200), nullable=True)
    # Full settings fields to match CSV
    axis = Column(String(10), nullable=True)
    offsetNo = Column(Integer, nullable=True)
    upperOffsetLimit = Column(Float, nullable=True)
    lowerOffsetLimit = Column(Float, nullable=True)
    Machine = Column(String(50), nullable=True)
    Direction = Column(String(20), nullable=True)
    TurretNo = Column(Integer, nullable=True)
    BufferPartNo = Column(Integer, nullable=True)


class ProbeValues(Base):
    """
    Table for storing probe measurement values
    """
    __tablename__ = 'ProbeValues'
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, nullable=True)
    ProbeBasedId = Column(Integer, nullable=True)
    AOCBasedId = Column(Integer, nullable=True)
    Value = Column(Float, nullable=True)
    Status = Column(String(10), nullable=True)
    JobCount = Column(Integer, nullable=True)
    Timestamp = Column(String(50), nullable=True)
    ProgId = Column(Integer, nullable=True)
    DeviceName = Column(String(10), nullable=True)
    Dimension = Column(String(5), nullable=True)

class MSSQLDatabase:
    """
    MSSQL Database Manager for OctoPreciGo
    Supports both Network Authentication and Cloud Authentication
    """
    
    def __init__(self, server: str, database: str, auth_mode: str = 'network', 
                 username: str = None, password: str = None, driver: str = 'ODBC Driver 17 for SQL Server'):
        """
        Initialize the MSSQL database connection
        
        Args:
            server: SQL Server hostname or IP address
            database: Database name (e.g., 'OctoPreciGo')
            auth_mode: Authentication mode - 'network' (Windows) or 'cloud' (SQL Server)
            username: Username for cloud authentication (required if auth_mode='cloud')
            password: Password for cloud authentication (required if auth_mode='cloud')
            driver: ODBC driver name (default: 'ODBC Driver 17 for SQL Server')
        """
        self.server = server
        self.database = database
        self.auth_mode = auth_mode
        self.username = username
        self.password = password
        self.driver = driver
        self.engine = None
        self.Session = None

        self.connect()
        # self.create_database()
        self.create_tables()
        self.disconnect()
    
    def get_connection_string(self) -> str:
        """
        Generate the appropriate connection string based on authentication mode
        """
        if self.auth_mode.lower() == 'network':
            # Network Authentication (Windows Authentication)
            # Uses trusted connection (no username/password required)
            conn_str = (
                f"mssql+pyodbc://{self.server}/{self.database}"
                f"?driver={self.driver.replace(' ', '+')}"
                f"&Trusted_Connection=yes"
            )
        elif self.auth_mode.lower() == 'cloud':
            # Cloud Authentication (SQL Server Authentication)
            # Uses username and password
            if not self.username or not self.password:
                raise ValueError("Username and password are required for cloud authentication")
            conn_str = (
                f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}"
                f"?driver={self.driver.replace(' ', '+')}"
            )
        else:
            raise ValueError(f"Invalid auth_mode: {self.auth_mode}. Use 'network' or 'cloud'")
        
        return conn_str
    
    def connect(self):
        """
        Establish database connection
        """
        conn_str = self.get_connection_string()
        self.engine = create_engine(conn_str, echo=False)
        self.Session = sessionmaker(bind=self.engine)
        return self.engine
    
    def create_database(self, check_first: bool = True):
        """
        Create the database if it doesn't exist
        
        Args:
            check_first: If True, only create if database doesn't exist
        """
        # Connect to master database first
        if self.auth_mode.lower() == 'network':
            conn_str = (
                f"mssql+pyodbc://{self.server}/master"
                f"?driver={self.driver.replace(' ', '+')}"
                f"&Trusted_Connection=yes"
            )
        else:
            conn_str = (
                f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/master"
                f"?driver={self.driver.replace(' ', '+')}"
            )
        
        temp_engine = create_engine(conn_str, echo=False)
        
        with temp_engine.connect() as conn:
            # Check if database exists
            result = conn.execute(f"SELECT name FROM sys.databases WHERE name = '{self.database}'")

            # result = conn.execute(
            #     text("SELECT name FROM sys.databases WHERE name = :dbname"),
            #     {"dbname": self.database}
            # )

            exists = result.fetchone() is not None
            
            if not exists or not check_first:
                conn.execute(f"CREATE DATABASE {self.database}")
                conn.commit()
                # conn.exec_driver_sql(f"CREATE DATABASE [{self.database}]")
        
        temp_engine.dispose()
    
    def create_tables(self):
        """
        Create all tables in the database
        """
        if self.engine is None:
            self.connect()
        
        Base.metadata.create_all(self.engine)
    
    def drop_tables(self):
        """
        Drop all tables from the database
        """
        if self.engine is None:
            self.connect()
        
        Base.metadata.drop_all(self.engine)
    
    def get_session(self):
        """
        Get a new database session
        """
        if self.Session is None:
            self.connect()
        return self.Session()
    
    def disconnect(self):
        """
        Disconnect from the database and close all connections
        """
        if self.engine is not None:
            self.engine.dispose()
            self.engine = None
            self.Session = None
    
    def close(self):
        """
        Alias for disconnect() - closes database connection
        """
        self.disconnect()
    
    def initialize_database(self, create_db: bool = True):
        """
        Complete database initialization
        
        Args:
            create_db: Whether to create the database if it doesn't exist
        """
        if create_db:
            self.create_database()
        
        self.connect()
        self.create_tables()
    
    def __enter__(self):
        """
        Context manager entry - returns session
        """
        return self.get_session()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit - automatically disconnects
        """
        self.disconnect()

    # -------------------------------------------------
    # SAVE METHODS FOR PROBE BASED IDS
    # -------------------------------------------------
    def save_probe_based_id(self, uid, settings_string, program_id, program_name, dimension,
                           formula, master_type, master_lower, master, master_higher,
                           upper_specification_limit, upper_control_limit, nominal_value,
                           lower_control_limit, lower_specification_limit, ovality, range_val,
                           method, case, case_t, least_count, probe_sensitivity, 
                           air_sensitivity_quotient, channel, created_date=None):
        """
        Save probe based ID to MSSQL database
        """
        try:
            session = self.get_session()
            # Check if settings_string already exists
            existing = session.query(ProbeBasedIds).filter(
                ProbeBasedIds.UniqueSettings == settings_string
            ).first()

            if existing:
                # Update existing
                existing.ProgramId = program_id
                existing.ProgramName = program_name
                existing.Dimension = dimension
                existing.Formula = formula
                existing.MasterType = master_type
                existing.MasterLower = master_lower
                existing.Master = master
                existing.MasterHigher = master_higher
                existing.UpperSpecificationLimit = upper_specification_limit
                existing.UpperControlLimit = upper_control_limit
                existing.NominalValue = nominal_value
                existing.LowerControlLimit = lower_control_limit
                existing.LowerSpecificationLimit = lower_specification_limit
                existing.Ovality = ovality
                existing.Range = range_val
                existing.Method = method
                existing.Case = case
                existing.CaseT = case_t
                existing.LeastCount = least_count
                existing.ProbeSensitivity = probe_sensitivity
                existing.AirSensitivityQuotient = air_sensitivity_quotient
                existing.Channel = channel
                session.commit()
                return existing.Id
            else:
                # Create new
                new_record = ProbeBasedIds(
                    UniqueSettings=settings_string,
                    ProgramId=program_id,
                    ProgramName=program_name,
                    Dimension=dimension,
                    Formula=formula,
                    MasterType=master_type,
                    MasterLower=master_lower,
                    Master=master,
                    MasterHigher=master_higher,
                    UpperSpecificationLimit=upper_specification_limit,
                    UpperControlLimit=upper_control_limit,
                    NominalValue=nominal_value,
                    LowerControlLimit=lower_control_limit,
                    LowerSpecificationLimit=lower_specification_limit,
                    Ovality=ovality,
                    Range=range_val,
                    Method=method,
                    Case=case,
                    CaseT=case_t,
                    LeastCount=least_count,
                    ProbeSensitivity=probe_sensitivity,
                    AirSensitivityQuotient=air_sensitivity_quotient,
                    Channel=channel,
                    created_date=created_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                session.add(new_record)
                session.commit()
                return new_record.Id
        except Exception as e:
            print(f"Error saving probe based ID to MSSQL: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def get_probe_based_id_by_settings(self, settings_string):
        """
        Get probe based ID by settings string
        """
        try:
            session = self.get_session()
            record = session.query(ProbeBasedIds).filter(
                ProbeBasedIds.UniqueSettings == settings_string
            ).first()
            result = record.Id if record else None
            session.close()
            return result
        except Exception as e:
            print(f"Error getting probe based ID from MSSQL: {e}")
            return None

    def get_all_probe_based_ids(self):
        """
        Get all probe based IDs from MSSQL
        """
        try:
            session = self.get_session()
            records = session.query(ProbeBasedIds).all()
            result = []
            for r in records:
                result.append({
                    "uid": r.Id,
                    "settings_string": r.UniqueSettings,
                    "ProgramId": r.ProgramId,
                    "ProgramName": r.ProgramName,
                    "Dimension": r.Dimension,
                    "Formula": r.Formula,
                    "MasterType": r.MasterType,
                    "MasterLower": r.MasterLower,
                    "Master": r.Master,
                    "MasterHigher": r.MasterHigher,
                    "UpperSpecificationLimit": r.UpperSpecificationLimit,
                    "UpperControlLimit": r.UpperControlLimit,
                    "NominalValue": r.NominalValue,
                    "LowerControlLimit": r.LowerControlLimit,
                    "LowerSpecificationLimit": r.LowerSpecificationLimit,
                    "Ovality": r.Ovality,
                    "Range": r.Range,
                    "Method": r.Method,
                    "Case": r.Case,
                    "CaseT": r.CaseT,
                    "LeastCount": r.LeastCount,
                    "ProbeSensitivity": r.ProbeSensitivity,
                    "AirSensitivityQuotient": r.AirSensitivityQuotient,
                    "Channel": r.Channel,
                    "created_date": r.created_date
                })
            session.close()
            return result
        except Exception as e:
            print(f"Error getting all probe based IDs from MSSQL: {e}")
            return []

    # -------------------------------------------------
    # SAVE METHODS FOR AOC BASED IDS
    # -------------------------------------------------
    def save_aoc_based_id(self, uid, settings_string, axis, offset_no, upper_offset_limit,
                         lower_offset_limit, machine, direction, turret_no, buffer_part_no):
        """
        Save AOC based ID to MSSQL database
        """
        try:
            session = self.get_session()
            # Check if settings_string already exists
            existing = session.query(AOCBasedIds).filter(
                AOCBasedIds.UniqueSettings == settings_string
            ).first()

            if existing:
                # Update existing
                existing.axis = axis
                existing.offsetNo = offset_no
                existing.upperOffsetLimit = upper_offset_limit
                existing.lowerOffsetLimit = lower_offset_limit
                existing.Machine = machine
                existing.Direction = direction
                existing.TurretNo = turret_no
                existing.BufferPartNo = buffer_part_no
                session.commit()
                return existing.Id
            else:
                # Create new
                new_record = AOCBasedIds(
                    UniqueSettings=settings_string,
                    axis=axis,
                    offsetNo=offset_no,
                    upperOffsetLimit=upper_offset_limit,
                    lowerOffsetLimit=lower_offset_limit,
                    Machine=machine,
                    Direction=direction,
                    TurretNo=turret_no,
                    BufferPartNo=buffer_part_no
                )
                session.add(new_record)
                session.commit()
                return new_record.Id
        except Exception as e:
            print(f"Error saving AOC based ID to MSSQL: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def get_aoc_based_id_by_settings(self, settings_string):
        """
        Get AOC based ID by settings string
        """
        try:
            session = self.get_session()
            record = session.query(AOCBasedIds).filter(
                AOCBasedIds.UniqueSettings == settings_string
            ).first()
            result = record.Id if record else None
            session.close()
            return result
        except Exception as e:
            print(f"Error getting AOC based ID from MSSQL: {e}")
            return None

    def get_all_aoc_based_ids(self):
        """
        Get all AOC based IDs from MSSQL
        """
        try:
            session = self.get_session()
            records = session.query(AOCBasedIds).all()
            result = []
            for r in records:
                result.append({
                    "uid": r.Id,
                    "settings_string": r.UniqueSettings,
                    "axis": r.axis,
                    "offsetNo": r.offsetNo,
                    "upperOffsetLimit": r.upperOffsetLimit,
                    "lowerOffsetLimit": r.lowerOffsetLimit,
                    "Machine": r.Machine,
                    "Direction": r.Direction,
                    "TurretNo": r.TurretNo,
                    "BufferPartNo": r.BufferPartNo
                })
            session.close()
            return result
        except Exception as e:
            print(f"Error getting all AOC based IDs from MSSQL: {e}")
            return []

    # -------------------------------------------------
    # SAVE METHODS FOR PROBE VALUES
    # -------------------------------------------------
    def save_probe_value(self, uid, probe_based_id, aoc_based_id, value, status, jobcount, 
                        timestamp, prog_id=None, device_name=None, dimension=None):
        """
        Save probe value to MSSQL database
        """
        try:
            session = self.get_session()
            new_record = ProbeValues(
                uid=uid,
                ProbeBasedId=probe_based_id,
                AOCBasedId=aoc_based_id,
                Value=value,
                Status=status,
                JobCount=jobcount,
                Timestamp=timestamp,
                ProgId=prog_id,
                DeviceName=device_name,
                Dimension=dimension
            )
            session.add(new_record)
            session.commit()
            return new_record.Id
        except Exception as e:
            print(f"Error saving probe value to MSSQL: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def get_probe_values_by_date(self, date_str):
        """
        Get probe values by date (format: dd-mm-yyyy)
        """
        try:
            session = self.get_session()
            # Convert date format for comparison
            from datetime import datetime
            try:
                dt = datetime.strptime(date_str, "%d-%m-%Y")
                date_filter = dt.strftime("%Y-%m-%d")
            except:
                date_filter = date_str
            
            records = session.query(ProbeValues).all()
            result = []
            for r in records:
                if r.Timestamp and date_filter in r.Timestamp:
                    result.append({
                        "uid": r.uid,
                        "ProbeBasedId": r.ProbeBasedId,
                        "AOCBasedId": r.AOCBasedId,
                        "Value": r.Value,
                        "Status": r.Status,
                        "JobCount": r.JobCount,
                        "Timestamp": r.Timestamp,
                        "ProgId": r.ProgId,
                        "DeviceName": r.DeviceName,
                        "Dimension": r.Dimension
                    })
            session.close()
            return result
        except Exception as e:
            print(f"Error getting probe values by date from MSSQL: {e}")
            return []

    def get_all_probe_values(self):
        """
        Get all probe values from MSSQL
        """
        try:
            session = self.get_session()
            records = session.query(ProbeValues).all()
            result = []
            for r in records:
                result.append({
                    "uid": r.uid,
                    "ProbeBasedId": r.ProbeBasedId,
                    "AOCBasedId": r.AOCBasedId,
                    "Value": r.Value,
                    "Status": r.Status,
                    "JobCount": r.JobCount,
                    "Timestamp": r.Timestamp,
                    "ProgId": r.ProgId,
                    "DeviceName": r.DeviceName,
                    "Dimension": r.Dimension
                })
            session.close()
            return result
        except Exception as e:
            print(f"Error getting all probe values from MSSQL: {e}")
            return []


# Convenience functions for quick access

def create_octoprecigo_db(server: str, auth_mode: str = 'network',
                          username: str = None, password: str = None,
                          driver: str = 'ODBC Driver 17 for SQL Server') -> MSSQLDatabase:
    """
    Create and initialize the OctoPreciGo database
    
    Args:
        server: SQL Server hostname or IP
        auth_mode: 'network' for Windows Auth, 'cloud' for SQL Server Auth
        username: SQL Server username (for cloud auth)
        password: SQL Server password (for cloud auth)
        driver: ODBC driver name
    
    Returns:
        MSSQLDatabase instance
    """
    db = MSSQLDatabase(
        server=server,
        database='OctoPreciGo',
        auth_mode=auth_mode,
        username=username,
        password=password,
        driver=driver
    )
    db.initialize_database()
    return db


# Example usage
# if __name__ == "__main__":
#     # Example 1: Network Authentication (Windows Auth)
#     print("Initializing with Network Authentication...")
#     db_network = MSSQLDatabase(
#         server="localhost\\SQLEXPRESS",
#         database="OctoPreciGo",
#         auth_mode="network",
#         username="sa",
#         password="intersense"
#     )

    # db_network.connect()
        # self.create_database()
    # db_network.create_tables()
    # db_network.disconnect()
    
    # Example 2: Cloud Authentication (SQL Server Auth)
    # print("Initializing with Cloud Authentication...")
    # db_cloud = MSSQLDatabase(
    #     server="your_server.database.windows.net",
    #     database="OctoPreciGo",
    #     auth_mode="cloud",
    #     username="your_username",
    #     password="your_password"
    # )
    
    # Example 3: Quick initialization
    # print("Quick initialization example...")
    # db = create_octoprecigo_db(server="localhost", auth_mode="network")

