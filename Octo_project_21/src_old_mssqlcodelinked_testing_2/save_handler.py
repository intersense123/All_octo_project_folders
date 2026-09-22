import csv
import os
from datetime import datetime
from models import SessionLocal, ProbeBasedSettings, NetworkedDatabaseSettings


class MSSQLHelper:
    """
    Helper class to get MSSQL database connection from SQLite settings
    """
    _instance = None
    _mssql_db = None
    
    @classmethod
    def get_mssql_db(cls):
        """
        Get MSSQL database instance using settings from SQLite
        """
        if cls._mssql_db is not None:
            return cls._mssql_db
        
        try:
            # Get MSSQL settings from SQLite
            session = SessionLocal()
            settings = {}
            db_settings = session.query(NetworkedDatabaseSettings).all()
            for s in db_settings:
                settings[s.Key] = s.Value
            session.close()
            
            # Check if networked database is enabled
            if settings.get("NETWORKE_BASED_DATABASE_ON_OFF", "OFF") != "ON":
                print("MSSQL: Networked database is OFF")
                return None
            
            # Get connection parameters
            server = settings.get("MS_SQL_SERVER_NAME", "")
            database = settings.get("MS_SQL_DATABASE_NAME", "")
            username = settings.get("MS_SQL_USERNAME", "")
            password = settings.get("MS_SQL_PASSWORD", "")
            driver = settings.get("MS_SQL_DRIVER_NAME", "{ODBC Driver 17 for SQL Server}")
            
            # Clean up values (remove semicolons if present)
            server = server.strip().rstrip(';')
            database = database.strip().rstrip(';')
            username = username.strip()
            password = password.strip()
            driver = driver.strip().rstrip(';')
            
            if not server or not database:
                print("MSSQL: Server or database not configured")
                return None
            
            # Import MSSQL module
            from MSSQL import MSSQLDatabase
            
            # Create MSSQL connection (use cloud auth since we have username/password)
            cls._mssql_db = MSSQLDatabase(
                server=server,
                database=database,
                auth_mode="cloud",
                username=username,
                password=password,
                driver=driver
            )
            
            print(f"MSSQL: Connected to {server}/{database}")
            return cls._mssql_db
            
        except Exception as e:
            print(f"MSSQL: Error initializing MSSQL: {e}")
            return None
    
    @classmethod
    def reset_instance(cls):
        """Reset the MSSQL instance (for testing or reconnection)"""
        cls._mssql_db = None


class CSVManager:
    """
    CSV Manager for OctoPreciGo
    Manages two CSV files:
    - probeBasedIds.csv: Stores unique probe settings/configuration
    - probeValues.csv: Stores live measurement values
    
    Now integrated with MSSQL database - saves to MSSQL first, then to CSV
    """

    def __init__(self):
        self.folder = "./Octo_CSV"
        os.makedirs(self.folder, exist_ok=True)

        # Two separate CSV files
        self.probe_based_ids_file = os.path.join(self.folder, "probeBasedIds.csv")
        self.aoc_based_ids_file = os.path.join(self.folder,"aocBasedIds.csv")
        self.probe_values_file = os.path.join(self.folder, "probeValues.csv")

        # Initialize CSV files with headers if not exist
        self._init_probe_based_ids_file()
        self._init_aoc_based_ids_file()
        self._init_probe_values_file()
        
        # Get MSSQL database instance
        self.mssql_db = MSSQLHelper.get_mssql_db()

    # -------------------------------------------------
    # SAVE TO MSSQL AND CSV
    # -------------------------------------------------
    def _save_probe_based_to_mssql(self, uid, settings_string, r, channel=1):
        """
        Save probe based settings to MSSQL database
        """
        if self.mssql_db is None:
            return None
        
        try:
            return self.mssql_db.save_probe_based_id(
                uid=uid,
                settings_string=settings_string,
                program_id=r.ProgramId,
                program_name=getattr(r, 'ProgramName', ''),
                dimension=r.Dimension,
                formula=getattr(r, 'Formula', ''),
                master_type=r.MasterType,
                master_lower=r.MasterLower or 0,
                master=r.Master or 0,
                master_higher=r.MasterHigher or 0,
                upper_specification_limit=r.UpperSpecificationLimit or 0,
                upper_control_limit=r.UpperControlLimit or 0,
                nominal_value=r.NominalValue or 0,
                lower_control_limit=r.LowerControlLimit or 0,
                lower_specification_limit=r.LowerSpecificationLimit or 0,
                ovality=r.Ovality or '',
                range_val=r.Range or 0,
                method=r.Method or '',
                case=r.Case,
                case_t=r.CaseT or 0,
                least_count=r.LeastCount or 0,
                probe_sensitivity=r.ProbeSensitivity or 0,
                air_sensitivity_quotient=r.AirSensitivityQuotient or 0,
                channel=channel,
                created_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        except Exception as e:
            print(f"Error saving probe based to MSSQL: {e}")
            return None
    
    def _save_aoc_based_to_mssql(self, uid, settings_string, aoc_record):
        """
        Save AOC based settings to MSSQL database
        """
        if self.mssql_db is None or aoc_record is None:
            return None
        
        try:
            return self.mssql_db.save_aoc_based_id(
                uid=uid,
                settings_string=settings_string,
                axis=getattr(aoc_record, 'axis', ''),
                offset_no=getattr(aoc_record, 'offsetNo', 0) or 0,
                upper_offset_limit=getattr(aoc_record, 'upperOffsetLimit', 0) or 0,
                lower_offset_limit=getattr(aoc_record, 'lowerOffsetLimit', 0) or 0,
                machine=getattr(aoc_record, 'Machine', ''),
                direction=getattr(aoc_record, 'Direction', ''),
                turret_no=getattr(aoc_record, 'TurretNo', 0) or 0,
                buffer_part_no=getattr(aoc_record, 'BufferPartNo', 0) or 0
            )
        except Exception as e:
            print(f"Error saving AOC based to MSSQL: {e}")
            return None
    
    def _save_probe_value_to_mssql(self, uid, probe_based_id, aoc_based_id, value, status, jobcount, timestamp):
        """
        Save probe value to MSSQL database
        """
        if self.mssql_db is None:
            return None
        
        try:
            return self.mssql_db.save_probe_value(
                uid=uid,
                probe_based_id=probe_based_id,
                aoc_based_id=aoc_based_id,
                value=value,
                status=status,
                jobcount=jobcount,
                timestamp=timestamp
            )
        except Exception as e:
            print(f"Error saving probe value to MSSQL: {e}")
            return None

    # -------------------------------------------------
    # INITIALIZE CSV FILES
    # -------------------------------------------------
    def _init_probe_based_ids_file(self):
        """Initialize probeBasedIds.csv with headers"""
        if not os.path.exists(self.probe_based_ids_file):
            with open(self.probe_based_ids_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "uid",
                    "settings_string",  # For internal comparison
                    "ProgramId",
                    "ProgramName",
                    "Dimension",
                    "Formula",
                    "MasterType",
                    "MasterLower",
                    "Master",
                    "MasterHigher",
                    "UpperSpecificationLimit",
                    "UpperControlLimit",
                    "NominalValue",
                    "LowerControlLimit",
                    "LowerSpecificationLimit",
                    "Ovality",
                    "Range",
                    "Method",
                    "Case",
                    "CaseT",
                    "LeastCount",
                    "ProbeSensitivity",
                    "AirSensitivityQuotient",
                    "Channel",
                    "created_date"
                ])
    def _init_aoc_based_ids_file(self):
        """Initialize aocBasedIds.csv with headers"""
        if not os.path.exists(self.aoc_based_ids_file):
            with open(self.aoc_based_ids_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "uid",
                    "settings_string", 
                    "axis",
                    "offsetNo",
                    "upperOffsetLimit",
                    "lowerOffsetLimit",
                    "Machine", 
                    "Direction",
                    "TurretNo",
                    "BufferPartNo"
                ])
    def _init_probe_values_file(self):
        """Initialize probeValues.csv with headers"""
        if not os.path.exists(self.probe_values_file):
            with open(self.probe_values_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "uid",
                    "ProbeBasedId",
                    "AOCBasedId",  # Link to AOC settings (blank if not selected)
                    "Value",
                    "Status",
                    "JobCount",
                    "Timestamp"
                ])

    # -------------------------------------------------
    # BUILD AOC SETTINGS STRING
    # -------------------------------------------------
    def build_aoc_settings_string(self, aoc_record):
        """Build unique settings string for AOC"""
        if aoc_record is None:
            return ""
        return "|".join([
            str(getattr(aoc_record, 'axis', '')),
            str(getattr(aoc_record, 'offsetNo', '')),
            str(getattr(aoc_record, 'upperOffsetLimit', '')),
            str(getattr(aoc_record, 'lowerOffsetLimit', '')),
            str(getattr(aoc_record, 'Machine', '')),
            str(getattr(aoc_record, 'Direction', '')),
            str(getattr(aoc_record, 'TurretNo', '')),
            str(getattr(aoc_record, 'BufferPartNo', ''))
        ])

    # -------------------------------------------------
    # GET OR CREATE AOC ID
    # -------------------------------------------------
    def get_or_create_aoc_id(self, aoc_record):
        """
        Get or create AOC based ID
        Returns None/blank if AOC not selected
        Saves to MSSQL first (if available), then to CSV
        """
        if aoc_record is None:
            return None
            
        settings_string = self.build_aoc_settings_string(aoc_record)
        if not settings_string:
            return None
            
        existing_settings = {}

        try:
            with open(self.aoc_based_ids_file, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get("settings_string"):
                        existing_settings[row["settings_string"]] = int(row["uid"])
        except:
            pass

        if settings_string in existing_settings:
            # Also save to MSSQL if available (to keep in sync)
            self._save_aoc_based_to_mssql(existing_settings[settings_string], settings_string, aoc_record)
            return existing_settings[settings_string]

        # Create new UID
        max_uid = max(existing_settings.values(), default=0)
        new_uid = max_uid + 1

        # Save to MSSQL first (if available)
        self._save_aoc_based_to_mssql(new_uid, settings_string, aoc_record)

        with open(self.aoc_based_ids_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                new_uid,
                settings_string,
                getattr(aoc_record, 'axis', ''),
                getattr(aoc_record, 'offsetNo', ''),
                getattr(aoc_record, 'upperOffsetLimit', ''),
                getattr(aoc_record, 'lowerOffsetLimit', ''),
                getattr(aoc_record, 'Machine', ''),
                getattr(aoc_record, 'Direction', ''),
                getattr(aoc_record, 'TurretNo', ''),
                getattr(aoc_record, 'BufferPartNo', '')
            ])

        return new_uid

    # -------------------------------------------------
    # BUILD SETTINGS STRING (for comparison)
    # -------------------------------------------------
    def build_settings_string(self, r, channel=1):
        """
        Build a unique settings string for comparison
        Includes all relevant settings plus channel
        """
        return "|".join([
            str(r.ProgramId),
            str(r.ProgramName),
            str(r.Dimension),
            str(r.Formula),
            str(r.MasterType),
            str(r.MasterLower),
            str(r.Master),
            str(r.MasterHigher),
            str(r.UpperSpecificationLimit),
            str(r.UpperControlLimit),
            str(r.NominalValue),
            str(r.LowerControlLimit),
            str(r.LowerSpecificationLimit),
            str(r.Ovality),
            str(r.Range),
            str(r.Method),
            str(r.Case),
            str(r.CaseT),
            str(r.LeastCount),
            str(r.ProbeSensitivity),
            str(r.AirSensitivityQuotient),
            str(channel)
        ])

    # -------------------------------------------------
    # GET OR CREATE PROBE ID (UID)
    # -------------------------------------------------
    def get_or_create_probe_id(self, r, channel=1):
        """
        Get existing uid or create new one based on settings
        Compares with existing settings and adds new uid if different
        Saves to MSSQL first (if available), then to CSV
        
        Args:
            r: Database record (ProbeBasedSettings)
            channel: Channel number (1, 2, etc.)
            
        Returns:
            uid: The unique identifier for this settings combination
        """
        settings_string = self.build_settings_string(r, channel)
        existing_settings = {}

        # Read existing settings from probeBasedIds.csv
        with open(self.probe_based_ids_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_settings[row["settings_string"]] = int(row["uid"])

        # If settings already exist, return existing uid
        if settings_string in existing_settings:
            # Also save to MSSQL if available (to keep in sync)
            self._save_probe_based_to_mssql(existing_settings[settings_string], settings_string, r, channel)
            return existing_settings[settings_string]

        # Create new UID
        max_uid = max(existing_settings.values(), default=0)
        new_uid = max_uid + 1

        # Save to MSSQL first (if available)
        self._save_probe_based_to_mssql(new_uid, settings_string, r, channel)

        # Write new settings to probeBasedIds.csv
        with open(self.probe_based_ids_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                new_uid,
                settings_string,
                r.ProgramId,
                r.ProgramName,
                r.Dimension,
                r.Formula,
                r.MasterType,
                r.MasterLower,
                r.Master,
                r.MasterHigher,
                r.UpperSpecificationLimit,
                r.UpperControlLimit,
                r.NominalValue,
                r.LowerControlLimit,
                r.LowerSpecificationLimit,
                r.Ovality,
                r.Range,
                r.Method,
                r.Case,
                r.CaseT,
                r.LeastCount,
                r.ProbeSensitivity,
                r.AirSensitivityQuotient,
                channel,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])

        return new_uid

    # -------------------------------------------------
    # COMPARE WITH DATABASE SETTINGS
    # -------------------------------------------------
    def compare_with_db_settings(self, db_record):
        """
        Compare current settings with database and check if new LSL/USL found
        If new settings found in DB, add new line with new uid in probeBasedIds
        
        Args:
            db_record: Database record with latest settings
            
        Returns:
            tuple: (uid, is_new_settings)
        """
        # Check if SessionLocal is available
        from models import SessionLocal
        if SessionLocal is None:
            return None, False
            
        # Get current settings from database
        session = SessionLocal()
        try:
            # Get the latest settings from database
            db_settings = session.query(ProbeBasedSettings).filter(
                ProbeBasedSettings.ProgramId == db_record.ProgramId,
                ProbeBasedSettings.Dimension == db_record.Dimension
            ).order_by(ProbeBasedSettings.Id.desc()).first()

            if db_settings:
                # Compare LSL and USL with existing probeBasedIds
                existing_uids = self._find_matching_uid(db_settings)
                
                if existing_uids:
                    # Check if LSL/USL has changed
                    for uid in existing_uids:
                        existing_settings = self._get_settings_by_uid(uid)
                        if existing_settings:
                            # Compare LSL and USL
                            db_lsl = float(db_settings.LowerSpecificationLimit or 0)
                            db_usl = float(db_settings.UpperSpecificationLimit or 0)
                            existing_lsl = float(existing_settings.get('LowerSpecificationLimit', 0) or 0)
                            existing_usl = float(existing_settings.get('UpperSpecificationLimit', 0) or 0)
                            
                            if db_lsl != existing_lsl or db_usl != existing_usl:
                                # New LSL/USL found - create new uid
                                return self.get_or_create_probe_id(db_settings, 
                                    int(existing_settings.get('Channel', 1))), True
                    
                    return existing_uids[0], False
                else:
                    # No matching settings - create new
                    return self.get_or_create_probe_id(db_settings, 1), True
                    
            return None, False
        finally:
            session.close()

    # -------------------------------------------------
    # FIND MATCHING UID
    # -------------------------------------------------
    def _find_matching_uid(self, r, channel=1):
        """Find all UIDs that match the settings"""
        settings_string = self.build_settings_string(r, channel)
        matching_uids = []

        with open(self.probe_based_ids_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("settings_string") == settings_string:
                    matching_uids.append(int(row["uid"]))

        return matching_uids

    # -------------------------------------------------
    # GET SETTINGS BY UID
    # -------------------------------------------------
    def _get_settings_by_uid(self, uid):
        """Get settings dictionary by uid"""
        with open(self.probe_based_ids_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["uid"]) == uid:
                    return row
        return None

    # -------------------------------------------------
    # GET PROBE BASED ID FROM DB
    # -------------------------------------------------
    def get_probe_based_id_from_db(self, db_record):
        """
        Get ProbeBasedId from database for a given record
        Uses UniqueSettings to match
        
        Returns:
            probe_based_id: The Id from ProbeBasedIds table (or None if DB not available)
        """
        # Check if SessionLocal is available
        from models import SessionLocal
        if SessionLocal is None:
            return None
            
        settings_string = self.build_settings_string(db_record)
        
        session = SessionLocal()
        try:
            # Check if settings exist in database
            probe_id_record = session.query(ProbeBasedSettings).filter(
                ProbeBasedSettings.UniqueSettings == settings_string
            ).first()

            if probe_id_record:
                return probe_id_record.Id
            return None
        finally:
            session.close()

    # -------------------------------------------------
    # SAVE LIVE DATA
    # -------------------------------------------------
    def save_live_data(self, db_record, value, status, jobcount, channel=1, mode="individual", aoc_record=None):
        """
        Save live measurement data to probeValues.csv and MSSQL
        
        Args:
            db_record: Database record with settings
            value: Measured value
            status: Measurement status (OK/NG)
            jobcount: Job count number
            channel: Channel number (1, 2, etc.)
            mode: "individual" or "combine"
                  - individual: Each dimension saved on separate row
                  - combine: All dimensions combined in single string
            aoc_record: AOC settings record (optional - can be None if not selected)
        """
        # Get or create uid based on settings
        uid = self.get_or_create_probe_id(db_record, channel)
        
        # Get ProbeBasedId from database if available
        probe_based_id = self.get_probe_based_id_from_db(db_record)
        
        # Get AOCBasedId - returns None/blank if AOC not selected
        aoc_based_id = self.get_or_create_aoc_id(aoc_record)

        # Generate timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if mode == "combine":
            # Combine mode: Save all dimensions in single row
            self._save_combined_data(uid, probe_based_id, aoc_based_id, db_record, value, status, jobcount, channel)
        else:
            # Individual mode: Save each dimension on separate row
            # Save to MSSQL first (if available)
            self._save_probe_value_to_mssql(uid, probe_based_id, aoc_based_id, value, status, jobcount, timestamp)
            
            # Then save to CSV
            with open(self.probe_values_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    uid,
                    probe_based_id or "",
                    aoc_based_id or "",  # Blank if AOC not selected
                    value,
                    status,
                    jobcount,
                    timestamp
                ])

    # -------------------------------------------------
    # SAVE COMBINED DATA
    # -------------------------------------------------
    def _save_combined_data(self, uid, probe_based_id, aoc_based_id, db_record, value, status, jobcount, channel):
        """
        Save combined data for multiple dimensions in single row
        Appends dimension values to existing row or creates new combined row
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Check if there's an existing combined row for this uid/timestamp
        existing_rows = []
        temp_rows = []
        
        with open(self.probe_values_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["uid"]) == uid and row.get("Timestamp", "").startswith(timestamp[:10]):
                    existing_rows.append(row)
                temp_rows.append(row)
        
        if existing_rows:
            # Append to existing combined row
            last_row = existing_rows[-1]
            # Add new dimension value to combined string
            combined_value = last_row.get("combined_values", "") + f"|{value}"
            
            # Update the row
            with open(self.probe_values_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "uid", "ProbeBasedId", "AOCBasedId", "combined_values", "Status", "JobCount", "Timestamp"
                ])
                for row in temp_rows:
                    if row == last_row:
                        writer.writerow([
                            row["uid"],
                            row["ProbeBasedId"],
                            row.get("AOCBasedId", ""),
                            combined_value,
                            row["Status"],
                            row["JobCount"],
                            row["Timestamp"]
                        ])
                    else:
                        writer.writerow([
                            row["uid"], row["ProbeBasedId"], row.get("AOCBasedId", ""), row.get("combined_values", ""),
                            row["Status"], row["JobCount"], row["Timestamp"]
                        ])
        else:
            # Create new combined row
            with open(self.probe_values_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    uid,
                    probe_based_id or "",
                    aoc_based_id or "",
                    value,  # First value
                    status,
                    jobcount,
                    timestamp
                ])

    # -------------------------------------------------
    # EXPORT BY DATE
    # -------------------------------------------------
    def export_by_date(self, date_str):
        """
        Export combined data by date
        Matches uid from probeValues with settings from probeBasedIds
        Loads settings fields below and adds live value, status, jobcount
        
        Output format:
        uid,ProgramId,ProgramName,Dimension,...,AOCBasedId,Value,Status,JobCount
        uid,ProgramId,ProgramName,Dimension,...,AOCBasedId,Value,Status,JobCount
        ...
        
        Args:
            date_str: Date in format dd-mm-yyyy
        """
        export_file = os.path.join(self.folder, f"{date_str}.csv")

        # Load all probe settings into memory
        probe_settings_map = {}
        with open(self.probe_based_ids_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                probe_settings_map[int(row["uid"])] = row

        # Load all AOC settings into memory
        aoc_settings_map = {}
        try:
            with open(self.aoc_based_ids_file, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    aoc_settings_map[int(row["uid"])] = row
        except:
            pass

        # Read probeValues and create export
        with open(self.probe_values_file, "r") as vf, open(export_file, "w", newline="") as ef:
            reader = csv.DictReader(vf)
            writer = csv.writer(ef)

            # Write header with AOC fields
            writer.writerow([
                "uid", "ProgramId", "ProgramName", "Dimension", "Formula", "MasterType",
                "MasterLower", "Master", "MasterHigher", "UpperSpecificationLimit",
                "UpperControlLimit", "NominalValue", "LowerControlLimit", "LowerSpecificationLimit",
                "Ovality", "Range", "Method", "Case", "CaseT", "LeastCount",
                "ProbeSensitivity", "AirSensitivityQuotient", "Channel",
                "AOCBasedId", "AOC_axis", "AOC_offsetNo", "AOC_upperOffsetLimit",
                "AOC_lowerOffsetLimit", "AOC_Machine", "AOC_Direction", "AOC_TurretNo",
                "AOC_BufferPartNo", "Value", "Status", "JobCount", "Timestamp"
            ])

            # Filter by date if needed
            for row in reader:
                uid = int(row["uid"])
                
                if uid not in probe_settings_map:
                    continue
                
                settings = probe_settings_map[uid]
                
                # Filter by date if date_str provided
                if date_str:
                    timestamp = row.get("Timestamp", "")
                    try:
                        from datetime import datetime
                        dt = datetime.strptime(date_str, "%d-%m-%Y")
                        date_filter = dt.strftime("%Y-%m-%d")
                    except:
                        date_filter = date_str
                    
                    if date_filter not in timestamp:
                        continue

                # Get AOC settings if available (blank if not selected)
                aoc_based_id = row.get("AOCBasedId", "")
                aoc_settings = {}
                if aoc_based_id:
                    try:
                        aoc_settings = aoc_settings_map.get(int(aoc_based_id), {})
                    except:
                        pass

                # Write combined row: probe settings + AOC settings + live values
                writer.writerow([
                    uid, settings.get("ProgramId", ""), settings.get("ProgramName", ""),
                    settings.get("Dimension", ""), settings.get("Formula", ""), settings.get("MasterType", ""),
                    settings.get("MasterLower", ""), settings.get("Master", ""), settings.get("MasterHigher", ""),
                    settings.get("UpperSpecificationLimit", ""), settings.get("UpperControlLimit", ""),
                    settings.get("NominalValue", ""), settings.get("LowerControlLimit", ""),
                    settings.get("LowerSpecificationLimit", ""), settings.get("Ovality", ""),
                    settings.get("Range", ""), settings.get("Method", ""), settings.get("Case", ""),
                    settings.get("CaseT", ""), settings.get("LeastCount", ""), settings.get("ProbeSensitivity", ""),
                    settings.get("AirSensitivityQuotient", ""), settings.get("Channel", ""),
                    aoc_based_id, aoc_settings.get("axis", ""), aoc_settings.get("offsetNo", ""),
                    aoc_settings.get("upperOffsetLimit", ""), aoc_settings.get("lowerOffsetLimit", ""),
                    aoc_settings.get("Machine", ""), aoc_settings.get("Direction", ""),
                    aoc_settings.get("TurretNo", ""), aoc_settings.get("BufferPartNo", ""),
                    row.get("Value", ""), row.get("Status", ""), row.get("JobCount", ""), row.get("Timestamp", "")
                ])

        print("Export created:", export_file)
        return export_file

    # -------------------------------------------------
    # EXPORT BY UID
    # -------------------------------------------------
    def export_by_uid(self, uid, date_str=None):
        """
        Export data for specific uid
        Useful for filtering and viewing specific probe data
        
        Args:
            uid: The uid to export
            date_str: Optional date filter (dd-mm-yyyy)
        """
        export_file = os.path.join(self.folder, f"export_uid_{uid}_{date_str or 'all'}.csv")

        # Load settings for this uid
        settings = self._get_settings_by_uid(uid)
        if not settings:
            print(f"No settings found for uid: {uid}")
            return None

        # Load all AOC settings into memory
        aoc_settings_map = {}
        try:
            with open(self.aoc_based_ids_file, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    aoc_settings_map[int(row["uid"])] = row
        except:
            pass

        # Export filtered data
        with open(self.probe_values_file, "r") as vf, open(export_file, "w", newline="") as ef:
            reader = csv.DictReader(vf)
            writer = csv.writer(ef)

            # Write header with AOC fields
            writer.writerow([
                "uid", "ProgramId", "ProgramName", "Dimension", "Formula", "MasterType",
                "MasterLower", "Master", "MasterHigher", "UpperSpecificationLimit",
                "UpperControlLimit", "NominalValue", "LowerControlLimit", "LowerSpecificationLimit",
                "Ovality", "Range", "Method", "Case", "CaseT", "LeastCount",
                "ProbeSensitivity", "AirSensitivityQuotient", "Channel",
                "AOCBasedId", "AOC_axis", "AOC_offsetNo", "AOC_upperOffsetLimit",
                "AOC_lowerOffsetLimit", "AOC_Machine", "AOC_Direction", "AOC_TurretNo",
                "AOC_BufferPartNo", "Value", "Status", "JobCount", "Timestamp"
            ])

            for row in reader:
                if int(row["uid"]) != uid:
                    continue
                
                # Filter by date if provided
                if date_str and date_str not in row.get("Timestamp", ""):
                    continue

                # Get AOC settings if available (blank if not selected)
                aoc_based_id = row.get("AOCBasedId", "")
                aoc_settings = {}
                if aoc_based_id:
                    try:
                        aoc_settings = aoc_settings_map.get(int(aoc_based_id), {})
                    except:
                        pass

                # Write combined row: probe settings + AOC settings + live values
                writer.writerow([
                    uid, settings.get("ProgramId", ""), settings.get("ProgramName", ""),
                    settings.get("Dimension", ""), settings.get("Formula", ""), settings.get("MasterType", ""),
                    settings.get("MasterLower", ""), settings.get("Master", ""), settings.get("MasterHigher", ""),
                    settings.get("UpperSpecificationLimit", ""), settings.get("UpperControlLimit", ""),
                    settings.get("NominalValue", ""), settings.get("LowerControlLimit", ""),
                    settings.get("LowerSpecificationLimit", ""), settings.get("Ovality", ""),
                    settings.get("Range", ""), settings.get("Method", ""), settings.get("Case", ""),
                    settings.get("CaseT", ""), settings.get("LeastCount", ""), settings.get("ProbeSensitivity", ""),
                    settings.get("AirSensitivityQuotient", ""), settings.get("Channel", ""),
                    aoc_based_id, aoc_settings.get("axis", ""), aoc_settings.get("offsetNo", ""),
                    aoc_settings.get("upperOffsetLimit", ""), aoc_settings.get("lowerOffsetLimit", ""),
                    aoc_settings.get("Machine", ""), aoc_settings.get("Direction", ""),
                    aoc_settings.get("TurretNo", ""), aoc_settings.get("BufferPartNo", ""),
                    row.get("Value", ""), row.get("Status", ""), row.get("JobCount", ""), row.get("Timestamp", "")
                ])

        print("Export created:", export_file)
        return export_file

    # -------------------------------------------------
    # GET ALL UNIQUE IDS
    # -------------------------------------------------
    def get_all_probe_ids(self):
        """Get all unique probe IDs and their settings"""
        probe_ids = []
        
        with open(self.probe_based_ids_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                probe_ids.append({
                    "uid": int(row["uid"]),
                    "ProgramId": row.get("ProgramId", ""),
                    "Dimension": row.get("Dimension", ""),
                    "Channel": row.get("Channel", ""),
                    "created_date": row.get("created_date", "")
                })
        
        return probe_ids

    # -------------------------------------------------
    # GET VALUES FOR UID
    # -------------------------------------------------
    def get_values_for_uid(self, uid, date_str=None):
        """Get all measurement values for a specific uid"""
        values = []
        
        with open(self.probe_values_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["uid"]) != uid:
                    continue
                
                if date_str and date_str not in row.get("Timestamp", ""):
                    continue
                
                values.append(row)
        
        return values


# Example usage
if __name__ == "__main__":
    csv_manager = CSVManager()
    
    # Example: Get all probe IDs
    # all_ids = csv_manager.get_all_probe_ids()
    # print(all_ids)
    
    # Example: Export by date
    # csv_manager.export_by_date("25-01-2025")
    
    # Example: Export by uid
    # csv_manager.export_by_uid(1, "25-01-2025")


# -------------------------------------------------
# HELPER FUNCTION TO SYNC FROM SQLITE TO MSSQL
# -------------------------------------------------
def sync_probe_settings_to_mssql(program_id=None):
    """
    Sync probe settings from SQLite to MSSQL
    Call this after saving probe settings via Save button
    
    Args:
        program_id: Optional program ID to filter (if None, syncs all)
    """
    csv_manager = CSVManager()
    
    try:
        # Get all probe based settings from SQLite
        session = SessionLocal()
        query = session.query(ProbeBasedSettings)
        if program_id:
            query = query.filter(ProbeBasedSettings.ProgramId == program_id)
        
        settings = query.all()
        
        for setting in settings:
            # Build settings string
            settings_string = csv_manager.build_settings_string(setting)
            
            # Get or create UID from CSV
            uid = csv_manager.get_or_create_probe_id(setting)
            
            print(f"Synced probe setting: {setting.Dimension} for Program {setting.ProgramId}")
        
        session.close()
        print("Sync completed successfully!")
        
    except Exception as e:
        print(f"Error syncing to MSSQL: {e}")


# -------------------------------------------------
# EXPORT FROM MSSQL TO CSV
# -------------------------------------------------
def export_from_mssql_to_csv(date_str=None):
    """
    Export data from MSSQL to CSV files
    Can be used to load data from MSSQL into CSV
    
    Args:
        date_str: Optional date filter (format: dd-mm-yyyy)
    """
    csv_manager = CSVManager()
    
    if csv_manager.mssql_db is None:
        print("MSSQL not available, cannot export from MSSQL")
        return None
    
    try:
        # Get probe based IDs from MSSQL
        probe_ids = csv_manager.mssql_db.get_all_probe_based_ids()
        
        # Write to CSV
        with open(csv_manager.probe_based_ids_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "uid", "settings_string", "ProgramId", "ProgramName", "Dimension",
                "Formula", "MasterType", "MasterLower", "Master", "MasterHigher",
                "UpperSpecificationLimit", "UpperControlLimit", "NominalValue",
                "LowerControlLimit", "LowerSpecificationLimit", "Ovality", "Range",
                "Method", "Case", "CaseT", "LeastCount", "ProbeSensitivity",
                "AirSensitivityQuotient", "Channel", "created_date"
            ])
            
            for row in probe_ids:
                writer.writerow([
                    row.get("uid"),
                    row.get("settings_string"),
                    row.get("ProgramId"),
                    row.get("ProgramName"),
                    row.get("Dimension"),
                    row.get("Formula"),
                    row.get("MasterType"),
                    row.get("MasterLower"),
                    row.get("Master"),
                    row.get("MasterHigher"),
                    row.get("UpperSpecificationLimit"),
                    row.get("UpperControlLimit"),
                    row.get("NominalValue"),
                    row.get("LowerControlLimit"),
                    row.get("LowerSpecificationLimit"),
                    row.get("Ovality"),
                    row.get("Range"),
                    row.get("Method"),
                    row.get("Case"),
                    row.get("CaseT"),
                    row.get("LeastCount"),
                    row.get("ProbeSensitivity"),
                    row.get("AirSensitivityQuotient"),
                    row.get("Channel"),
                    row.get("created_date")
                ])
        
        print(f"Exported {len(probe_ids)} probe based IDs to CSV")
        
        # Get AOC based IDs from MSSQL
        aoc_ids = csv_manager.mssql_db.get_all_aoc_based_ids()
        
        with open(csv_manager.aoc_based_ids_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "uid", "settings_string", "axis", "offsetNo", "upperOffsetLimit",
                "lowerOffsetLimit", "Machine", "Direction", "TurretNo", "BufferPartNo"
            ])
            
            for row in aoc_ids:
                writer.writerow([
                    row.get("uid"),
                    row.get("settings_string"),
                    row.get("axis"),
                    row.get("offsetNo"),
                    row.get("upperOffsetLimit"),
                    row.get("lowerOffsetLimit"),
                    row.get("Machine"),
                    row.get("Direction"),
                    row.get("TurretNo"),
                    row.get("BufferPartNo")
                ])
        
        print(f"Exported {len(aoc_ids)} AOC based IDs to CSV")
        
        # Get probe values from MSSQL
        if date_str:
            probe_values = csv_manager.mssql_db.get_probe_values_by_date(date_str)
        else:
            probe_values = csv_manager.mssql_db.get_all_probe_values()
        
        with open(csv_manager.probe_values_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "uid", "ProbeBasedId", "AOCBasedId", "Value", "Status", "JobCount", "Timestamp"
            ])
            
            for row in probe_values:
                writer.writerow([
                    row.get("uid"),
                    row.get("ProbeBasedId"),
                    row.get("AOCBasedId"),
                    row.get("Value"),
                    row.get("Status"),
                    row.get("JobCount"),
                    row.get("Timestamp")
                ])
        
        print(f"Exported {len(probe_values)} probe values to CSV")
        
        return True
        
    except Exception as e:
        print(f"Error exporting from MSSQL to CSV: {e}")
        return None

