from sqlalchemy import create_engine, Column, Integer, String, func, Float, Date
from sqlalchemy.orm import sessionmaker,declarative_base
import random
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy import text

# Database configuration
DB_NAME = "OctoPreciGo"
DB_PATH = f"/home/torizon/app/{DB_NAME}.db"
DB_URL = f"sqlite:///{DB_PATH}"

# SQLAlchemy setup (moved to DatabaseManager class)


class SaveDatabaseManager:
    """
    Class for all database operations: connect, create_tables, disconnect.
    """
    
    def __init__(self, db_url=None):
        self.db_url = db_url or DB_URL
        self.engine = None
        self.SessionLocal = None
        self.Base = declarative_base()
        
        class ProbeBasedIds(self.Base):
            __tablename__ = 'ProbeBasedIds'
            ProbeId = Column(Integer, primary_key=True, autoincrement=True)
            # Id = Column(Integer, nullable=False)
            ProbeUniqueSettings = Column(String(500), nullable=False, unique=True)

        class AOCBasedIds(self.Base):
            __tablename__ = 'AOCBasedIds'
            AOCId = Column(Integer, primary_key=True, autoincrement=True)
            # AOCId = Column(Integer, nullable=False)
            AOCUniqueSettings = Column(String(200), nullable=False)

        class ProbeValues(self.Base):
            __tablename__ = "ProbeValues"
            Id = Column(Integer, primary_key=True, autoincrement=True)
            ProbeBasedId = Column(Integer, nullable=False)
            GlobalCounter = Column(Integer, nullable=False)
            Mode = Column(String(1), nullable=False)
            JobCount = Column(Integer, nullable=True)
            Value = Column(Float, nullable=True)
            Status = Column(String(10), nullable=True)
            Date = Column(DateTime)
        
        class SPCResetTracker(self.Base):
            __tablename__ = "SPCResetTracker"

            Id = Column(Integer, primary_key=True, autoincrement=True)
            ProbeBasedId = Column(Integer, nullable=False, unique=True)
            LastResetCounter = Column(Integer, nullable=False)
            Date = Column(DateTime)

        class AOCValues(self.Base):
            __tablename__ = "AOCValues"
            Id = Column(Integer, primary_key=True, autoincrement=True)
            AOCBasedId = Column(Integer, nullable=False)
            GlobalCounter = Column(Integer, nullable=False)
            # Parameter = Column(String(5), nullable=False)
            Machine = Column(String(10), nullable=False)
            Gauge = Column(String(15), nullable=False)
            PartName = Column(String(15), nullable=False)
            # NominalValue = Column(Float, nullable=False)
            ToolNo = Column(Integer, nullable=False)
            Reading = Column(Float, nullable=False)
            Correction = Column(Float, nullable=False)
            ToolValue = Column(Float, nullable=False)
            Date = Column(DateTime)
        
        self.ProbeBasedIds = ProbeBasedIds
        self.AOCBasedIds = AOCBasedIds
        self.ProbeValues = ProbeValues
        self.AOCValues = AOCValues
        self.SPCResetTracker = SPCResetTracker
    
    def connect(self):
        """
        Connect to DB and prepare sessionmaker.
        """
        self.engine = create_engine(self.db_url, echo=False)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        print(f"Connected to database.")
    
    def create_tables(self):
        """
        Create tables if they don't exist.
        """
        if self.engine:
            self.Base.metadata.create_all(bind=self.engine)
            print("Tables created.")
        else:
            raise ValueError("Connect first.")
    
    def disconnect(self):
        """
        Close DB connections.
        """
        if self.engine:
            self.engine.dispose()
            self.engine = None
            self.SessionLocal = None
            print("Disconnected from database.")
    
    def get_session(self):
        """
        Get a new DB session.
        """
        if not self.SessionLocal:
            raise ValueError("Connect first.")
        return self.SessionLocal()

    def insert_probe_based_ids(self, probe_unique_settings: str) -> int:
        """
        Insert a new ProbeBasedIds record.
        """
        session = self.get_session()
        try:
            new_record = self.ProbeBasedIds(ProbeUniqueSettings=probe_unique_settings)
            session.add(new_record)
            session.commit()
            return new_record.ProbeId
        finally:
            session.close()


    def insert_probe_values(self, probe_based_id: int, global_counter: int, mode: str, job_count: int = None, value: float = None, status: str = None) -> int:
        """
        Insert a new ProbeValues record.
        """
        session = self.get_session()
        try:
            new_record = self.ProbeValues(
                ProbeBasedId=probe_based_id,
                GlobalCounter=global_counter,
                Mode=mode,
                JobCount=job_count,
                Value=value,
                Status=status,
                Date=datetime.now()
            )
            session.add(new_record)
            session.commit()
            return new_record.Id
        finally:
            session.close()
        
    def get_probe_values_for_spc(self, probe_id, limit=50):

        session = self.get_session()

        try:
            # 🔥 STEP 1: Get latest reset counter
            result = session.execute(
                """
                SELECT LastResetCounter
                FROM SPCResetTracker
                WHERE ProbeBasedId = :probe_id
                ORDER BY Date DESC
                LIMIT 1
                """,
                {"probe_id": probe_id}
            ).fetchone()

            reset_counter = result[0] if result else 0

            print(f"[SPC] Using reset_counter = {reset_counter}")  # debug

            # 🔥 STEP 2: Fetch ONLY new data after reset
            rows = session.execute(
                """
                SELECT Value
                FROM ProbeValues
                WHERE ProbeBasedId = :probe_id
                AND GlobalCounter > :reset_counter
                ORDER BY GlobalCounter DESC
                LIMIT :limit
                """,
                {
                    "probe_id": probe_id,
                    "limit": limit,
                    "reset_counter": reset_counter
                }
            ).fetchall()

            return [r[0] for r in rows]

        finally:
            session.close()

    def reset_spc_for_probe(self, probe_id):
        session = self.get_session()
        try:
            # Get latest counter
            last_counter = session.execute(
                """
                SELECT COALESCE(MAX(GlobalCounter),0)
                FROM ProbeValues
                WHERE ProbeBasedId = :pid
                """,
                {"pid": probe_id}
            ).fetchone()[0]

            # 🔥 CHECK if already exists
            record = session.query(self.SPCResetTracker)\
                .filter(self.SPCResetTracker.ProbeBasedId == probe_id)\
                .first()

            if record:
                # ✅ UPDATE
                record.LastResetCounter = last_counter
                record.Date = datetime.now()
                print(f"[SPC RESET] Updated for Probe {probe_id} → {last_counter}")
            else:
                # ✅ INSERT FIRST TIME
                new_record = self.SPCResetTracker(
                    ProbeBasedId=probe_id,
                    LastResetCounter=last_counter,
                    Date=datetime.now()
                )
                session.add(new_record)
                print(f"[SPC RESET] Created for Probe {probe_id} → {last_counter}")

            session.commit()

        finally:
            session.close()
                
    def get_latest_global_counter(self):
        session = self.get_session()
        try:
            result = session.execute(
                "SELECT MAX(GlobalCounter) FROM ProbeValues"
            ).fetchone()
            return result[0] if result and result[0] else 0
        finally:
            session.close()
            
    def get_next_counters(self):

        session = self.get_session()

        try:
            result = session.execute(
                """
                SELECT 
                    COALESCE(MAX(GlobalCounter),0),
                    COALESCE(MAX(JobCount),0)
                FROM ProbeValues
                """
            ).fetchone()

            last_global = result[0]
            last_job = result[1]

            return last_global + 1, last_job + 1

        finally:
            session.close()
              
    def get_probe_id_by_settings(self, unique_string):
        """
        Get ProbeId by ProbeUniqueSettings string.
        Returns ProbeId (int) or 0 if not found.
        """
        session = self.get_session()
        try:
            record = session.query(self.ProbeBasedIds)\
                .filter(self.ProbeBasedIds.ProbeUniqueSettings == unique_string)\
                .first()
            
            return record.ProbeId if record else 0
            
        finally:
            session.close()

# Example usage
# if __name__ == "__main__":
    # db = DatabaseManager()
    # db.connect()
    # db.create_tables()
    
    # # Example: session = db.get_session()
    # # # ... use session
    # # session.close()

    # # Insert examples with | -delimited random settings strings
    # probe_unique = "1|SHAFT|D1|P1|25.0|22.0|20.0|18.0|16.0|Standard|ID|None|0.0|0.01"
    # probe_id = db.insert_probe_based_ids(probe_unique_settings=probe_unique)
    # print(f"Inserted ProbeBasedIds ID: {probe_id}")

    # print("Inserting 30,000 probe values...")
    # for global_counter in range(1, 8001):
    #     value = random.uniform(16.0, 25.0)
    #     status = random.choice(['OK', 'NOTOK', 'REWORK'])
    #     db.insert_probe_values(probe_based_id=1, global_counter=global_counter, mode='C', job_count=global_counter, value=value, status=status)
    
    # print("Inserted 30,000 probe values.")

    # print("Inserting 15,000 probe values (mode 'I')...")
    # for global_counter in range(8001, 10001):
    #     value = random.uniform(16.0, 25.0)
    #     status = random.choice(['OK', 'NOTOK', 'REWORK'])
    #     db.insert_probe_values(probe_based_id=1, global_counter=global_counter, mode='I', job_count=global_counter, value=value, status=status)
    # print("Inserted additional 15,000 probe values (total 45,000).")

    # # aoc_unique = "1|D1|x|10|CNC1|p|0|0|PreciGo|SHAFT|27.00|25.00|22.00|20.00|18.00|16.00|14.00"

    # # aoc_id = db.insert_aoc_based_ids(aoc_id=1, aoc_unique_settings=aoc_unique)
    # # print(f"Inserted AOCBasedIds ID: {aoc_id}")
    # # id,d,axis,ToolNo,Machine,direction,turret,bufferpartno,gauge,partname,uol,usl,ucl,nominal,lcl,lsl,lol

    # db.disconnect()

