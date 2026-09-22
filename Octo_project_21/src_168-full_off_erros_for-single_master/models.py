from sqlalchemy import Column, Integer, Sequence, String, Time, create_engine , Float
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# -----------------------------
# User management: stores login credentials
# and inserts default admin/operator users.
# -----------------------------

class UserManagement(Base):
    __tablename__ = "UserManagement"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False)
    AccessType = Column(String, nullable=False)

    @classmethod
    def insert_defaults(cls, session):
        """Insert default users if they don't exist"""
        if session.query(cls).count() == 0:
            defaults = [
                {"Username": "admin", "Password": "admin", "AccessType": "Admin"}]
            for user in defaults:
                session.add(cls(**user))
            session.commit()

# -----------------------------
# CNC machine connection list:
# stores machine names, IP, port, and controller type.
# -----------------------------

class CNCMaster(Base):
    __tablename__ = "CNCMaster"

    id = Column(Integer, primary_key=True, autoincrement=True)
    CNCName = Column(String, nullable=False)
    IPAddress = Column(String, nullable=False)
    PortNumber = Column(Integer, nullable=False)
    CNCSelection = Column(String, nullable=False)
    ControllerName = Column(String, nullable=False)
    Trial_mode = Column(String,nullable=False)

# -----------------------------
# Shift configuration:
# defines working shifts and their time ranges.
# -----------------------------

class ShiftTimings(Base):
    __tablename__ = "ShiftTimings"

#     id = Column(Integer, primary_key=True, autoincrement=True)
    Shift = Column(Integer, primary_key=True)
    FromTime = Column(Time, nullable=False)
    ToTime = Column(Time, nullable=False)

# -----------------------------
# Local network configuration:
# stores device IP, subnet, and gateway.
# -----------------------------

class IPSettings(Base):
    __tablename__ = "IPSettings"

#     id = Column(Integer, primary_key=True, autoincrement=True)
    SelfIPAddress = Column(String, primary_key=True)
    SubnetMask = Column(String, nullable=False)
    DefaultGateway = Column(String, nullable=False)

# -----------------------------
# Wi-Fi settings: SSID and password.
# -----------------------------

class WifiSettings(Base):
    __tablename__ = "WifiSettings"

#     id = Column(Integer, primary_key=True, autoincrement=True)
    WifiSSID = Column(String, primary_key=True)
    WifiPassword = Column(String, nullable=False)

# -----------------------------
# Program settings: program metadata,
# mode, units of measure, autosave duration.
# -----------------------------

class ProgramSettings(Base):
    __tablename__ = "ProgramSettings"

    ProgramId = Column(Integer, primary_key=True, autoincrement=True)
    ProgramName = Column(String, nullable=False)
    Mode = Column(String, nullable=False)
    Uom = Column(String, nullable=False)
    AutoSave_Duration = Column(Float, nullable=False)
    Responsiveness = Column(Integer, nullable=False)

# -----------------------------
# Settings for remote database connection:
# stores driver, server, database, username, password,
# and inserts defaults if missing.
# -----------------------------

class NetworkedDatabaseSettings(Base):
    __tablename__ = "NetworkedDatabaseSettings"

#     id = Column(Integer, primary_key=True, autoincrement=True)
    Key = Column(String, primary_key=True, unique=True)
    Value = Column(String, nullable=False)

    @classmethod
    def insert_defaults(cls, session):
        """Insert default networked database settings if they don't exist"""
        defaults = [
            {"Key": "NETWORKE_BASED_DATABASE_ON_OFF", "Value": "OFF"},
            {"Key": "MS_SQL_DRIVER_NAME", "Value": "{SQL Server Native Client 11.0};"},
            {"Key": "MS_SQL_SERVER_NAME", "Value": "LENOVOCI5\\SQLEXPRESS;"},
            {"Key": "MS_SQL_DATABASE_NAME", "Value": "Octo_PreciGo;"},
            {"Key": "MS_SQL_USERNAME", "Value": "sa"},
            {"Key": "MS_SQL_PASSWORD", "Value": "password"},
        ]
        for item in defaults:
            if not session.query(cls).filter_by(Key=item["Key"]).first():
                session.add(cls(**item))
        session.commit()

# -----------------------------
# RS232 serial communication settings:
# baud rate, parity, stop bits, etc.
# -----------------------------

class RS232Settings(Base):
    __tablename__ = "RS232Settings"

#     id = Column(Integer, primary_key=True, autoincrement=True)
    Key = Column(String, primary_key=True, unique=True)
    Value = Column(String, nullable=False)

    @classmethod
    def insert_defaults(cls, session):
        """Insert default networked database settings if they don't exist"""
        defaults = [
            {"Key": "RS232_ON_OFF", "Value": "OFF"},
            {"Key": "BAUD_RATE", "Value": "115200"},
            {"Key": "DATA_BITS", "Value": "8"},
            {"Key": "PARITY", "Value": "None"},
            {"Key": "STOP_BITS", "Value": "One"},
            {"Key": "FLOW_CONTROL", "Value": "None"},
            {"Key": "PORT_NAME", "Value": "ttymxc0"},
        ]
        for item in defaults:
            if not session.query(cls).filter_by(Key=item["Key"]).first():
                session.add(cls(**item))
        session.commit()

# -----------------------------
# AOC (Automatic Offset Control) settings:
# enables/disables AOC and SPC data count.
# -----------------------------

class AOCSettings(Base):
    __tablename__ = "AOCSettings"

    Key = Column(String, primary_key=True, unique=True)
    Value = Column(String, nullable=False)

    @classmethod
    def insert_defaults(cls, session):
        defaults = [
            {"Key": "AOC_ON_OFF", "Value": "OFF"},
            {"Key": "SPC_DATA_COUNT", "Value": "50"},
        ]
        
        for item in defaults:
            if not session.query(cls).filter_by(Key=item["Key"]).first():
                session.add(cls(**item))

        session.commit()


# -----------------------------
# Angle calculation configuration:
# stores master angles, tolerances, distance,
# and whether the feature is enabled.
# -----------------------------
     
class AngleCalculationSettings(Base):
    __tablename__ = "AngleCalculationSettings"

    ProgramId = Column(Integer,primary_key=True,autoincrement=True)
    Angle_Calculation_setting_on_off = Column(String,nullable = False)
    Master_angle_Degrees = Column(Integer,nullable = False)
    Master_angle_Minutes = Column(Integer,nullable = False)
    Master_angle_sec = Column(Integer,nullable = False)
    Plus_Tolerance_Minutes = Column(Integer,nullable = False)
    Plus_Tolerance_Seconds = Column(Integer,nullable = False)
    Minus_Tolerance_Minutes = Column(Integer,nullable = False)
    Minus_Tolerance_Seconds = Column(Integer,nullable = False)
    Distance = Column(Float,nullable = False)
    AngleType = Column(String,nullable = False)
    
# -----------------------------
# IO settings: buzzer, relay, timers,
# traceability, display modes, etc.
# -----------------------------

class IOSettings(Base):
    __tablename__ = "IOSettings"

    Key = Column(String, primary_key=True, unique=True)
    Enable = Column(String, nullable=True)
    Value = Column(String, nullable=True)

    @classmethod
    def insert_defaults(cls, session):
        """Insert default IO settings if they don't exist"""
        defaults = [
            {"Key": "BUZZER", "Enable": "0", "Value": "Ok"},
            {"Key": "RELAY", "Enable": "0", "Value": "2"},
            {"Key": "CYCLE_STOP_TIMER", "Enable": "0", "Value": "2"},
            {"Key": "AUTO_SAVE_READING", "Enable": "0", "Value": None},
            {"Key": "PART_TRACEABILITY", "Enable": "0", "Value": "Manual Reset"},
            {"Key": "SAVE_MASTER_CALIBRATION", "Enable": "OFF", "Value": None},
            {"Key": "TIME_TO_MASTER_SET", "Enable": "0", "Value": "2"},
            {"Key": "MASTER_GROUPING", "Enable": "0", "Value": None},
        ]
        for item in defaults:
            if not session.query(cls).filter_by(Key=item["Key"]).first():
                session.add(cls(**item))
        session.commit()

# -----------------------------
# Probe-based measurement settings:
# defines tolerance limits, nominal value,
# sensitivity, and master values.
# -----------------------------


class ProbeBasedSettings(Base):
    __tablename__ = "ProbeBasedSettings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ProgramId = Column(Integer, nullable=False)
    ProgramName = Column(String,nullable=True)
    Dimension = Column(String, nullable=True)
    DimensionName = Column(String, nullable=False)
    Formula = Column(String, nullable=True)
    MasterType = Column(String, nullable=True)
    MasterLower = Column(Float, nullable=True)
    Master = Column(Float, nullable=True)
    MasterHigher = Column(Float, nullable=True)
    UpperSpecificationLimit = Column(Float, nullable=True)
    UpperControlLimit = Column(Float, nullable=True)
    NominalValue = Column(Float, nullable=True)
    LowerControlLimit = Column(Float, nullable=True)
    LowerSpecificationLimit = Column(Float, nullable=True)
    Ovality = Column(String, nullable=True)
    Range = Column(Float, nullable=True)
    Method = Column(String, nullable=True)
    Case = Column(String, nullable=True)
    CaseT = Column(Float, nullable=True)
    LeastCount = Column(Float,nullable=True)
    ProbeSensitivity = Column(Integer, nullable=True)
    AirSensitivityQuotient = Column(String, nullable=True)

    
# -----------------------------
# Probe-based measurement settings:
# defines tolerance limits, nominal value,
# sensitivity, and master values.
# -----------------------------

class AOCBasedSettings(Base):
    __tablename__ = "AOCBasedSettings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ProgramId = Column(Integer, nullable=False)
    Dimension = Column(String, nullable=True)
    aocEnable = Column(String,nullable = True)
    Axis = Column(String, nullable=True)
    OffsetNo = Column(Integer, nullable=True)
    UpperOffsetLimit = Column(Float, nullable=True)
    LowerOffsetLimit = Column(Float, nullable=True)
    Machine = Column(String, nullable=True)
    Direction = Column(String, nullable=True)
    TurretNo = Column(Integer, nullable=True)
    WorkInProcess = Column(Integer, nullable=True)
    SkipOffsetCount = Column(Integer, nullable=True)
    
class FactoryConfigSettings(Base):
    __tablename__ = "FactoryConfigSettings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    factory_config = Column(String, nullable=True)

class SetMasterSettings(Base):
    __tablename__ = "SetMasterSettings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ProgramId = Column(Integer, nullable=False)
    Dimension = Column(String, nullable=True)
    MasterValue = Column(Float, nullable=True)
    RemovedPartValue = Column(Float, nullable=True)
    SPI_low = Column(Float, nullable=True)
    SPI_high = Column(Float, nullable=True)
    SPI_Master = Column(Float,nullable = True)
    DB_low = Column(Float, nullable=True)
    DB_high = Column(Float, nullable=True)
    single_master_conversion_factor = Column(Float, nullable=True)
#to store active variable in table activevariable for use of programid
class ActiveVariables(Base):
    __tablename__ = "ActiveVariables"

    Key = Column(String, primary_key=True, unique=True)
    Value = Column(String, nullable=False)

    @classmethod
    def insert_defaults(cls, session):
        """Insert default active variables if they don't exist"""
        defaults = [
            {"Key": "ActiveProgramId", "Value": "1"},
            {"Key": "BuzzerOnOff", "Value": "OFF"},
            {"Key": "RelayOnOff", "Value": "OFF"},
            {"Key": "CycleStopTimer", "Value": "OFF"},
            {"Key": "AutoSaveOnOff", "Value": "OFF"},
            {"Key": "PartTraceabilityOnOff", "Value": "OFF"},
            {"Key": "TimeToMasterSetOnOff", "Value": "OFF"},
            {"Key": "MasterGroupingOnOff", "Value": "OFF"},
            {"Key": "SaveMasterCalibrationOnOff", "Value": "OFF"},
            {"Key": "AOCOnOff", "Value": "OFF"},
            {"Key": "AngleCalculationOnOff", "Value": "OFF"},
            {"Key": "NetworkedDatabaseSettingsOnOff", "Value": "OFF"},
            {"Key": "RS232OnOff", "Value": "OFF"},
        ]
        for item in defaults:
            if not session.query(cls).filter_by(Key=item["Key"]).first():
                session.add(cls(**item))
        session.commit()
        
# -----------------------------
# Database setup:
# - Creates SQLite DB (replace with MSSQL if needed)
# - Creates tables
# - Inserts default values for all settings
# -----------------------------

# Example: setup engine and session for "Octo-PreciGo" database
engine = create_engine("sqlite:////home/torizon/app/data/precigo.db")  # change to MSSQL if needed
SessionLocal = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(engine)

# Insert defaults via classmethod
session = SessionLocal()
UserManagement.insert_defaults(session)
NetworkedDatabaseSettings.insert_defaults(session)
RS232Settings.insert_defaults(session)
IOSettings.insert_defaults(session)
AOCSettings.insert_defaults(session)
ActiveVariables.insert_defaults(session)
session.close()
