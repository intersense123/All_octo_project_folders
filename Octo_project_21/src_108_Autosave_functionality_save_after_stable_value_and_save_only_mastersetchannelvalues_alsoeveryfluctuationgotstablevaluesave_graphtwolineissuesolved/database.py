import models
from models import *

from sqlalchemy.orm import Session , sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import create_engine

class DatabaseAgent:
    def __init__(self):
        # Initializes the database connection (SQLite here)
        # and prepares a session factory for ORM operations.

        engine = create_engine("sqlite:////home/torizon/app/precigo.db")
        self.SessionLocal = sessionmaker(bind=engine)

    
    def get_all_program_ids(self):
        session = self.SessionLocal()
        try:
            ids_program = session.query(ProgramSettings.ProgramId).all()
            ids_probe = session.query(ProbeBasedSettings.ProgramId).all()
            ids_aoc = session.query(AOCBasedSettings.ProgramId).all()

            all_ids = {
                row[0] for row in ids_program + ids_probe + ids_aoc
            }

            return sorted(all_ids)

        except Exception as e:
            print(f"Error fetching program ids: {e}")
            return []

        finally:
            session.close()
        
    def upsert_wifi_settings(self, ssid: str, password: str):
        """
        Insert or update WiFi settings.
        - If a record already exists, update SSID and Password.
        - If no record exists, insert a new one.
        """
        with self.SessionLocal() as session:
            try:
                existing = session.query(WifiSettings).first()
                if existing:
                    existing.WifiSSID = ssid
                    existing.WifiPassword = password
                else:
                    new_entry = WifiSettings(WifiSSID=ssid, WifiPassword=password)
                    session.add(new_entry)
                session.commit()
                return True
            except IntegrityError:
                session.rollback()
                print(f"Error: WiFi settings with SSID '{ssid}' already exists (IntegrityError).")
                return False
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Database error during upsert_wifi_settings: {e}")
                return False
            except Exception as e:
                session.rollback()
                print(f"An unexpected error occurred during upsert_wifi_settings: {e}")
                return False
    
    def upsert_ip_settings(self, ip: str, subnet: str, gateway: str):
        """
        Insert or update IP settings.
        - Updates SelfIPAddress, SubnetMask, and DefaultGateway if record exists.
        - Otherwise, creates a new row.
        """
        with self.SessionLocal() as session:
            try:
                existing = session.query(IPSettings).first()
                if existing:
                    existing.SelfIPAddress = ip
                    existing.SubnetMask = subnet
                    existing.DefaultGateway = gateway
                else:
                    new_entry = IPSettings(SelfIPAddress=ip, SubnetMask=subnet, DefaultGateway=gateway)
                    session.add(new_entry)
                session.commit()
                return True
            except IntegrityError:
                session.rollback()
                print(f"Error: IP settings already exists (IntegrityError).")
                return False
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Database error during upsert_ip_settings: {e}")
                return False
            except Exception as e:
                session.rollback()
                print(f"An unexpected error occurred during upsert_ip_settings: {e}")
                return False
        
    
    def upsert_cnc_list(self, cnc_name: str, ip: str, port: int, selection: str, controller: str):
        """
        Insert or update a CNC entry.
        - Uses CNCName to identify uniqueness.
        - If CNC exists → update details.
        - If not → insert new CNC entry.
        """
        with self.SessionLocal() as session:
            try:
                existing = session.query(CNCList).filter_by(CNCName=cnc_name).first()
                if existing:
                    existing.CNCName = cnc_name
                    existing.IPAddress = ip
                    existing.PortNumber = port
                    existing.CNCSelection = selection
                    existing.ControllerName = controller
                else:
                    new_entry = CNCList(
                        CNCName=cnc_name,
                        IPAddress=ip,
                        PortNumber=port,
                        CNCSelection=selection,
                        ControllerName=controller
                    )
                    session.add(new_entry)
                session.commit()
                return True
            except IntegrityError:
                session.rollback()
                print(f"Error: CNC entry with name '{cnc_name}' already exists (IntegrityError).")
                return False
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Database error during upsert_cnc_list: {e}")
                return False
            except Exception as e:
                session.rollback()
                print(f"An unexpected error occurred during upsert_cnc_list: {e}")
                return False

    # def update_angle_calculation_settings(
    #         self,
    #         PROGRAM_ID: str,
    #         ANGLE_CALCULATION_SETTINGS_ON_OFF: str,
    #         MASTER_ANGLE_DEGREES: str,
    #         MASTER_ANGLE_MINUTES: str,
    #         MASTER_ANGLE_SECONDS: str,
    #         PLUS_TOLERANCE_MINUTES: str,
    #         PLUS_TOLERANCE_SECONDS: str,
    #         MINUS_TOLERANCE_MINUTES: str,
    #         MINUS_TOLERANCE_SECONDS: str,
    #         DISTANCE: str,
    #         ANGLETYPE: str
    #     ):
    #         with self.SessionLocal() as session:
    #             try:
    #                 def upsert(key, value):
    #                     existing = session.query(AngleCalculationSettings).filter_by(Key=key).first()
    #                     if existing:
    #                         existing.Value = str(value)
    #                     else:
    #                         session.add(AngleCalculationSettings(Key=key, Value=str(value)))

    #                 upsert("PROGRAM_ID", PROGRAM_ID)
    #                 upsert("ANGLE_CALCULATION_SETTINGS_ON_OFF", ANGLE_CALCULATION_SETTINGS_ON_OFF)
    #                 upsert("MASTER_ANGLE_DEGREES", MASTER_ANGLE_DEGREES)
    #                 upsert("MASTER_ANGLE_MINUTES", MASTER_ANGLE_MINUTES)
    #                 upsert("MASTER_ANGLE_SECONDS", MASTER_ANGLE_SECONDS)
    #                 upsert("PLUS_TOLERANCE_MINUTES", PLUS_TOLERANCE_MINUTES)
    #                 upsert("PLUS_TOLERANCE_SECONDS", PLUS_TOLERANCE_SECONDS)
    #                 upsert("MINUS_TOLERANCE_MINUTES", MINUS_TOLERANCE_MINUTES)
    #                 upsert("MINUS_TOLERANCE_SECONDS", MINUS_TOLERANCE_SECONDS)
    #                 upsert("DISTANCE", DISTANCE)
    #                 upsert("ANGLETYPE", ANGLETYPE)

    #                 session.commit()
    #             except SQLAlchemyError as e:
    #                 session.rollback()
    #                 print(f"Database error during update_angle_calculation_settings: {e}")
    #                 return False
    #             except Exception as e:
    #                 session.rollback()
    #                 print(f"An unexpected error occurred during update_angle_calculation_settings: {e}")
    #                 return False
    
    def upsert_angle_calculation_settings(
        self,
        program_id: int,
        angle_calculation_setting_on_off: str,
        master_angle_degrees: int,
        master_angle_minutes: int,
        master_angle_seconds: int,
        plus_tolerance_minutes: int,
        plus_tolerance_seconds: int,
        minus_tolerance_minutes: int,
        minus_tolerance_seconds: int,
        distance: float,
        angle_type: str
    ) -> bool:
        """
        Upsert an AngleCalculationSettings row for the given ProgramId.
        """
        with self.SessionLocal() as session:
            try:
                existing = session.query(AngleCalculationSettings).filter_by(ProgramId=program_id).first()

                if existing:
                    # Update existing record
                    existing.Angle_Calculation_setting_on_off = angle_calculation_setting_on_off
                    existing.Master_angle_Degrees = master_angle_degrees
                    existing.Master_angle_Minutes = master_angle_minutes
                    existing.Master_angle_sec = master_angle_seconds
                    existing.Plus_Tolerance_Minutes = plus_tolerance_minutes
                    existing.Plus_Tolerance_Seconds = plus_tolerance_seconds
                    existing.Minus_Tolerance_Minutes = minus_tolerance_minutes
                    existing.Minus_Tolerance_Seconds = minus_tolerance_seconds
                    existing.Distance = distance
                    existing.AngleType = angle_type
                else:
                    # Insert new row for this ProgramId
                    new_entry = AngleCalculationSettings(
                        ProgramId=program_id,
                        Angle_Calculation_setting_on_off=angle_calculation_setting_on_off,
                        Master_angle_Degrees=master_angle_degrees,
                        Master_angle_Minutes=master_angle_minutes,
                        Master_angle_sec=master_angle_seconds,
                        Plus_Tolerance_Minutes=plus_tolerance_minutes,
                        Plus_Tolerance_Seconds=plus_tolerance_seconds,
                        Minus_Tolerance_Minutes=minus_tolerance_minutes,
                        Minus_Tolerance_Seconds=minus_tolerance_seconds,
                        Distance=distance,
                        AngleType=angle_type
                    )
                    session.add(new_entry)

                session.commit()
                return True

            except SQLAlchemyError as e:
                session.rollback()
                print(f"Database error during upsert_angle_calculation_settings: {e}")
                return False
            except Exception as e:
                session.rollback()
                print(f"Unexpected error during upsert_angle_calculation_settings: {e}")
                return False



    def update_networked_database_settings(
                self,
                NETWORKE_BASED_DATABASE_ON_OFF: str,
                MS_SQL_DRIVER_NAME: str,
                MS_SQL_SERVER_NAME: str,
                MS_SQL_DATABASE_NAME: str,
                MS_SQL_USERNAME: str,
                MS_SQL_PASSWORD: str
            ):

            """
            Insert or update networked database connection settings.
            - Covers driver name, server name, DB name, username, and password.
            - Ensures defaults are preserved if missing.
            """

            with self.SessionLocal() as session:
                try:
                    def upsert(key, value):
                        existing = session.query(NetworkedDatabaseSettings).filter_by(Key=key).first()
                        if existing:
                            existing.Value = str(value)
                        else:
                            session.add(NetworkedDatabaseSettings(Key=key, Value=str(value)))

                    upsert("NETWORKE_BASED_DATABASE_ON_OFF", NETWORKE_BASED_DATABASE_ON_OFF)
                    upsert("MS_SQL_DRIVER_NAME", MS_SQL_DRIVER_NAME)
                    upsert("MS_SQL_SERVER_NAME", MS_SQL_SERVER_NAME)
                    upsert("MS_SQL_DATABASE_NAME", MS_SQL_DATABASE_NAME)
                    upsert("MS_SQL_USERNAME", MS_SQL_USERNAME)
                    upsert("MS_SQL_PASSWORD", MS_SQL_PASSWORD)

                    session.commit()
                    return True
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during update_networked_database_settings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during update_networked_database_settings: {e}")
                    return False

    def update_rs232_settings(
                self,
                RS232_ON_OFF: str,
                BAUD_RATE: str,
                DATA_BITS: str,
                PARITY: str,
                STOP_BITS: str,
                FLOW_CONTROL: str,
                PORT_NAME: str
            ):
            """
            Insert or update RS232 communication settings.
            - Handles baud rate, data bits, parity, stop bits, flow control, etc.
            - Ensures consistent configuration in the database.
            """
            with self.SessionLocal() as session:
                try:
                    def upsert(key, value):
                        existing = session.query(RS232Settings).filter_by(Key=key).first()
                        if existing:
                            existing.Value = str(value)
                        else:
                            session.add(RS232Settings(Key=key, Value=str(value)))

                    upsert("RS232_ON_OFF", RS232_ON_OFF)
                    upsert("BAUD_RATE", BAUD_RATE)
                    upsert("DATA_BITS", DATA_BITS)
                    upsert("PARITY", PARITY)
                    upsert("STOP_BITS", STOP_BITS)
                    upsert("FLOW_CONTROL", FLOW_CONTROL)
                    upsert("PORT_NAME", PORT_NAME)

                    session.commit()
                    return True
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during update_rs232_settings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during update_rs232_settings: {e}")
                    return False

    def update_io_settings(
                self,
                BUZZER: tuple,
                RELAY: tuple,
                CYCLE_STOP_TIMER: tuple,
                AUTO_SAVE_READING: tuple,
                PART_TRACEABILITY: tuple,
                SAVE_MASTER_CALIBRATION: tuple,
                TIME_TO_MASTER_SET: tuple,
                MASTER_GROUPING: tuple
            ):
            """
            Insert or update I/O (Input/Output) control settings.
            - Each key stores an Enable flag and a Value.
            - Example: BUZZER, RELAY, AUTO_SAVE_READING.
            """
            with self.SessionLocal() as session:
                try:
                    def upsert(key, enable_value_tuple):
                        enable, value = enable_value_tuple
                        existing = session.query(IOSettings).filter_by(Key=key).first()
                        if existing:
                            existing.Enable = str(enable) if enable is not None else None
                            existing.Value = str(value) if value is not None else None
                        else:
                            session.add(IOSettings(
                                Key=key,
                                Enable=str(enable) if enable is not None else None,
                                Value=str(value) if value is not None else None
                            ))

                    upsert("BUZZER", BUZZER)
                    upsert("RELAY", RELAY)
                    upsert("CYCLE_STOP_TIMER", CYCLE_STOP_TIMER)
                    upsert("AUTO_SAVE_READING", AUTO_SAVE_READING)
                    upsert("PART_TRACEABILITY", PART_TRACEABILITY)
                    upsert("SAVE_MASTER_CALIBRATION",SAVE_MASTER_CALIBRATION)
                    upsert("TIME_TO_MASTER_SET", TIME_TO_MASTER_SET)
                    upsert("MASTER_GROUPING", MASTER_GROUPING)

                    session.commit()
                    return True
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during update_io_settings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during update_io_settings: {e}")
                    return False

    def update_aoc_settings(
            self,
            AOC_ON_OFF: str,
            SPC_DATA_COUNT: str
        ):

        """
        Insert or update AOC (Automatic Offset Compensation) settings.
        - Keys: AOC_ON_OFF, SPC_DATA_COUNT.
        """

        with self.SessionLocal() as session:
            try:
                def upsert(key, value):
                    existing = session.query(AOCSettings).filter_by(Key=key).first()
                    if existing:
                        existing.Value = str(value)
                    else:
                        session.add(AOCSettings(Key=key, Value=str(value)))

                upsert("AOC_ON_OFF", AOC_ON_OFF)
                upsert("SPC_DATA_COUNT", SPC_DATA_COUNT)

                session.commit()
                return True
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Database error during update_aoc_settings: {e}")
                return False
            except Exception as e:
                session.rollback()
                print(f"An unexpected error occurred during update_aoc_settings: {e}")
                return False

    def upsert_shift_timings(
                self,
                shift1: tuple[str, str],
                shift2: tuple[str, str],
                shift3: tuple[str, str]
            ):
            """
            Upsert 3 shift timings.
            Each shift parameter is a tuple: (FromTime, ToTime)
            Example:
                self.upsert_shift_timings(
                    ("08:00:00", "16:00:00"),
                    ("16:00:00", "00:00:00"),
                    ("00:00:00", "08:00:00")
                )
            """
            from datetime import datetime

            def to_time(val: str):
                return datetime.strptime(val, "%H:%M:%S").time()

            with self.SessionLocal() as session:
                try:
                    shift_data = {
                        1: shift1,
                        2: shift2,
                        3: shift3
                    }

                    for shift, (from_time, to_time_val) in shift_data.items():
                        existing = session.query(ShiftTimings).filter_by(Shift=shift).first()
                        if existing:
                            existing.FromTime = to_time(from_time)
                            existing.ToTime = to_time(to_time_val)
                        else:
                            session.add(
                                ShiftTimings(
                                    Shift=shift,
                                    FromTime=to_time(from_time),
                                    ToTime=to_time(to_time_val)
                                )
                            )
                    session.commit()
                    return True
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during upsert_shift_timings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during upsert_shift_timings: {e}")
                    return False
    
    def upsert_user_management(self,user_id: int, username: str, password: str, access_type: str):
            """
            Upsert a user in UserManagement based on Username.
            If user exists -> update Password & AccessType
            If user does not exist -> insert new user
            """
            with self.SessionLocal() as session:
                try:
                    existing = session.query(UserManagement).filter_by(Username=username).first()

                    # -----------------
                    # ADD MODE
                    # -----------------
                    if user_id is None:

                        if existing:
                            return "duplicate"

                        session.add(
                            UserManagement(
                                Username=username,
                                Password=password,
                                AccessType=access_type
                            )
                        )

                        session.commit()
                        return "added"

                    # -----------------
                    # UPDATE MODE
                    # -----------------
                    else:

                        user = session.query(UserManagement).filter_by(id=user_id).first()

                        if not user:
                            return "not_found"

                        # If username belongs to another user
                        if existing and existing.id != user_id:
                            return "duplicate"

                        user.Username = username
                        user.Password = password
                        user.AccessType = access_type

                        session.commit()
                        return "updated"
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during upsert_user_management: {e}")
                    return False

    def upsert_program_settings(self, program_id: int, program_name: str, mode: str, uom: str, auto_save_duration: float,Responsiveness: int):
            """
            Upsert a ProgramSettings row based on ProgramId.
            - If ProgramId exists -> update fields.
            - If ProgramId does not exist -> insert a new row (without specifying ProgramId).
            """
            with self.SessionLocal() as session:
                try:
                    existing = session.query(ProgramSettings).filter_by(ProgramId=program_id).first()
                    if existing:
                        existing.ProgramName = program_name
                        existing.Mode = mode
                        existing.Uom = uom
                        existing.AutoSave_Duration = auto_save_duration
                        existing.Responsiveness = Responsiveness
                    else:
                        session.add(
                            ProgramSettings(
                                ProgramName=program_name,
                                Mode=mode,
                                Uom=uom,
                                AutoSave_Duration=auto_save_duration,
                                Responsiveness=Responsiveness
                            )
                        )
                    session.commit()
                    return True
                except IntegrityError:
                    session.rollback()
                    print(f"Error: Program with ID '{program_id}' already exists (IntegrityError).")
                    return False
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during upsert_program_settings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during upsert_program_settings: {e}")
                    return False
            
    def upsert_probe_based_settings(
            self,
            program_id: int,
            ProgramName: str,
            dimension: str,
            dimensionName: str,
            formula: str = None,
            master_type: str = None,
            master_lower: float = None,
            master: float = None,
            master_higher: float = None,
            # upper_offset_limit: float = None,
            upper_specification_limit: float = None,
            upper_control_limit: float = None,
            nominal_value: float = None,
            lower_control_limit: float = None,
            lower_specification_limit: float = None,
            # lower_offset_limit: float = None,
            ovality: str = None,
            range_val: float = None,
            method: str = None,
            case: str = None,
            case_t: float = None,
            LeastCount : float = None,
            probe_sensitivity: int = None,
            air_sensitivity_quotient: str = None
        ):
            """
            Upsert ProbeBasedSettings rows filtered by ProgramId AND Dimension.
            - If one or more rows exist -> update ALL matching rows (single UPDATE).
            - If no rows exist -> insert a new row.
            Note: fields passed as None will be written as NULL (if that's not desired,
            see the alternative approach below).
            """
            with self.SessionLocal() as session:
                try:
                    query = session.query(ProbeBasedSettings).filter_by(
                        ProgramId=program_id, Dimension=dimension
                    )
                    # ✅ ADD HERE (program name sync)
                    existing_row = session.query(ProbeBasedSettings.ProgramName).filter_by(
                        ProgramId=program_id
                    ).first()

                    if existing_row and existing_row[0] != ProgramName:
                        session.query(ProbeBasedSettings).filter_by(
                            ProgramId=program_id
                        ).update(
                            {ProbeBasedSettings.ProgramName: ProgramName},
                            synchronize_session=False
                        )
                        
                    # Build mapping of ORM attributes -> values for update()
                    update_values = {
                        ProbeBasedSettings.ProgramName: ProgramName,
                        ProbeBasedSettings.DimensionName: dimensionName,
                        ProbeBasedSettings.Formula: formula,
                        ProbeBasedSettings.MasterType: master_type,
                        ProbeBasedSettings.MasterLower: master_lower,
                        ProbeBasedSettings.Master: master,
                        ProbeBasedSettings.MasterHigher: master_higher,
                        # ProbeBasedSettings.UpperOffsetLimit: upper_offset_limit,
                        ProbeBasedSettings.UpperSpecificationLimit: upper_specification_limit,
                        ProbeBasedSettings.UpperControlLimit: upper_control_limit,
                        ProbeBasedSettings.NominalValue: nominal_value,
                        ProbeBasedSettings.LowerControlLimit: lower_control_limit,
                        ProbeBasedSettings.LowerSpecificationLimit: lower_specification_limit,
                        # ProbeBasedSettings.LowerOffsetLimit: lower_offset_limit,
                        ProbeBasedSettings.Ovality: ovality,
                        ProbeBasedSettings.Range: range_val,
                        ProbeBasedSettings.Method: method,
                        ProbeBasedSettings.Case: case,
                        ProbeBasedSettings.CaseT: case_t,
                        ProbeBasedSettings.LeastCount:LeastCount,
                        ProbeBasedSettings.ProbeSensitivity: probe_sensitivity,
                        ProbeBasedSettings.AirSensitivityQuotient: air_sensitivity_quotient
                    }

                    # Perform bulk update (updates all matched rows)
                    updated_count = query.update(update_values, synchronize_session=False)

                    if updated_count == 0:
                        # No existing rows matched -> insert one new row
                        session.add(
                            ProbeBasedSettings(
                                ProgramId=program_id,
                                ProgramName=ProgramName,
                                Dimension=dimension,
                                DimensionName=dimensionName,
                                Formula=formula,
                                MasterType=master_type,
                                MasterLower=master_lower,
                                Master=master,
                                MasterHigher=master_higher,
                                # UpperOffsetLimit=upper_offset_limit,
                                UpperSpecificationLimit=upper_specification_limit,
                                UpperControlLimit=upper_control_limit,
                                NominalValue=nominal_value,
                                LowerControlLimit=lower_control_limit,
                                LowerSpecificationLimit=lower_specification_limit,
                                # LowerOffsetLimit=lower_offset_limit,
                                Ovality=ovality,
                                Range=range_val,
                                Method=method,
                                Case=case,
                                CaseT=case_t,
                                LeastCount=LeastCount,
                                ProbeSensitivity=probe_sensitivity,
                                AirSensitivityQuotient=air_sensitivity_quotient
                            )
                        )

                    session.commit()
                    return True
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during upsert_probe_based_settings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during upsert_probe_based_settings: {e}")
                    return False

    def upsert_aoc_based_settings(
            self,
            program_id: int,
            dimension: str,
            axis: str = None,
            offset_no: int = None,
            upper_offset_limit: float = None,
            lower_offset_limit: float = None,
            machine: str = None,
            direction: str = None,
            turret_no: int = None,
            buffer_part_no: int = None
        ):
            """
            Upsert an AOCBasedSettings row based on ProgramId and Dimension.
            - If exists -> update fields.
            - If not -> insert new row.
            """
            with self.SessionLocal() as session:
                try:
                    existing = (
                        session.query(AOCBasedSettings)
                        .filter_by(ProgramId=program_id, Dimension=dimension)
                        .first()
                    )
                    if existing:
                        existing.Axis = axis
                        existing.OffsetNo = offset_no
                        existing.UpperOffsetLimit = upper_offset_limit
                        existing.LowerOffsetLimit = lower_offset_limit
                        existing.Machine = machine
                        existing.Direction = direction
                        existing.TurretNo = turret_no
                        existing.BufferPartNo = buffer_part_no
                    else:
                        session.add(
                            AOCBasedSettings(
                                ProgramId=program_id,
                                Dimension=dimension,
                                Axis=axis,
                                OffsetNo=offset_no,
                                UpperOffsetLimit=upper_offset_limit,
                                LowerOffsetLimit=lower_offset_limit,
                                Machine=machine,
                                Direction=direction,
                                TurretNo=turret_no,
                                BufferPartNo=buffer_part_no
                            )
                        )
                    session.commit()
                    return True
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Database error during upsert_aoc_based_settings: {e}")
                    return False
                except Exception as e:
                    session.rollback()
                    print(f"An unexpected error occurred during upsert_aoc_based_settings: {e}")
                    return False
    
    def load_data_to_WifiSettings_dict(self):
        with self.SessionLocal() as session:
            try:
                wifi_entries = session.query(WifiSettings).all()

                if wifi_entries:
                    first_entry = wifi_entries[0]
                    self.WifiSettings_dict = {
                        'WifiSSID': first_entry.WifiSSID,
                        'WifiPassword': first_entry.WifiPassword
                    }
                else:
                    self.WifiSettings_dict = {
                        'WifiSSID': '',
                        'WifiPassword': ''
                    }
                return self.WifiSettings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_WifiSettings_dict: {e}")
                return {'WifiSSID': '', 'WifiPassword': ''} # Return default or empty on error
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_WifiSettings_dict: {e}")
                return {'WifiSSID': '', 'WifiPassword': ''}

    def load_data_to_RS232Settings_dict(self):
        with self.SessionLocal() as session:
            try:
                rs232_entries = session.query(RS232Settings).all()

                self.RS232Settings_dict = {entry.Key: entry.Value for entry in rs232_entries}

                if not self.RS232Settings_dict:
                    self.RS232Settings_dict = {
                        'RS232_ON_OFF': 'OFF',
                        'BAUD_RATE': '115200',
                        'DATA_BITS': '8',
                        'PARITY': 'None',
                        'STOP_BITS': 'One',
                        'FLOW_CONTROL': 'None',
                        'PORT_NAME': 'ttymxc0'
                    }
                return self.RS232Settings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_RS232Settings_dict: {e}")
                return { # Return defaults on error
                    'RS232_ON_OFF': 'OFF', 'BAUD_RATE': '115200', 'DATA_BITS': '8',
                    'PARITY': 'None', 'STOP_BITS': 'One', 'FLOW_CONTROL': 'None',
                    'PORT_NAME': 'ttymxc0'
                }
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_RS232Settings_dict: {e}")
                return { # Return defaults on error
                    'RS232_ON_OFF': 'OFF', 'BAUD_RATE': '115200', 'DATA_BITS': '8',
                    'PARITY': 'None', 'STOP_BITS': 'One', 'FLOW_CONTROL': 'None',
                    'PORT_NAME': 'ttymxc0'
                }

    def load_data_to_NetworkedDatabaseSettings_dict(self):
        with self.SessionLocal() as session:
            try:
                db_entries = session.query(NetworkedDatabaseSettings).all()

                self.NetworkedDatabaseSettings_dict = {entry.Key: entry.Value for entry in db_entries}

                if not self.NetworkedDatabaseSettings_dict:
                    self.NetworkedDatabaseSettings_dict = {
                        'NETWORKE_BASED_DATABASE_ON_OFF': 'OFF',
                        'MS_SQL_DRIVER_NAME': '{SQL Server Native Client 11.0}',
                        'MS_SQL_SERVER_NAME': 'LENOVOCI5\\SQLEXPRESS',
                        'MS_SQL_DATABASE_NAME': 'Octo_PreciGo',
                        'MS_SQL_USERNAME': 'sa',
                        'MS_SQL_PASSWORD': 'password'
                    }
                return self.NetworkedDatabaseSettings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_NetworkedDatabaseSettings_dict: {e}")
                return { # Return defaults on error
                    'NETWORKE_BASED_DATABASE_ON_OFF': 'OFF',
                    'MS_SQL_DRIVER_NAME': '{SQL Server Native Client 11.0}',
                    'MS_SQL_SERVER_NAME': 'LENOVOCI5\\SQLEXPRESS',
                    'MS_SQL_DATABASE_NAME': 'Octo_PreciGo',
                    'MS_SQL_USERNAME': 'sa',
                    'MS_SQL_PASSWORD': 'password'
                }
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_NetworkedDatabaseSettings_dict: {e}")
                return { # Return defaults on error
                    'NETWORKE_BASED_DATABASE_ON_OFF': 'OFF',
                    'MS_SQL_DRIVER_NAME': '{SQL Server Native Client 11.0}',
                    'MS_SQL_SERVER_NAME': 'LENOVOCI5\\SQLEXPRESS',
                    'MS_SQL_DATABASE_NAME': 'Octo_PreciGo',
                    'MS_SQL_USERNAME': 'sa',
                    'MS_SQL_PASSWORD': 'password'
                }
    
    def load_data_to_IPSettings_dict(self):
        with self.SessionLocal() as session:
            try:
                ip_entries = session.query(IPSettings).all()

                if ip_entries:
                    first_entry = ip_entries[0]
                    self.IPSettings_dict = {
                        'SelfIPAddress': first_entry.SelfIPAddress,
                        'SubnetMask': first_entry.SubnetMask,
                        'DefaultGateway': first_entry.DefaultGateway
                    }
                else:
                    self.IPSettings_dict = {
                        'SelfIPAddress': '',
                        'SubnetMask': '',
                        'DefaultGateway': ''
                    }
                return self.IPSettings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_IPSettings_dict: {e}")
                return {'SelfIPAddress': '', 'SubnetMask': '', 'DefaultGateway': ''}
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_IPSettings_dict: {e}")
                return {'SelfIPAddress': '', 'SubnetMask': '', 'DefaultGateway': ''}

    def load_data_to_ShiftTimings_dict(self):
        with self.SessionLocal() as session:
            try:
                shift_entries = session.query(ShiftTimings).all()

                if shift_entries and len(shift_entries) == 3:
                    self.ShiftTimings_dict = {}
                    for entry in shift_entries:
                        shift = entry.Shift
                        self.ShiftTimings_dict[f'Shift{shift}'] = shift
                        self.ShiftTimings_dict[f'FromTime{shift}'] = entry.FromTime.strftime("%H:%M")
                        self.ShiftTimings_dict[f'ToTime{shift}'] = entry.ToTime.strftime("%H:%M")
                else:
                    self.ShiftTimings_dict = {
                        'Shift1': 1, 'FromTime1': '00:00', 'ToTime1': '14:00',
                        'Shift2': 2, 'FromTime2': '14:00', 'ToTime2': '22:00',
                        'Shift3': 3, 'FromTime3': '22:00', 'ToTime3': '00:00'
                    }
                return self.ShiftTimings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_ShiftTimings_dict: {e}")
                return { # Return defaults on error
                    'Shift1': 1, 'FromTime1': '00:00', 'ToTime1': '14:00',
                    'Shift2': 2, 'FromTime2': '14:00', 'ToTime2': '22:00',
                    'Shift3': 3, 'FromTime3': '22:00', 'ToTime3': '00:00'
                }
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_ShiftTimings_dict: {e}")
                return { # Return defaults on error
                    'Shift1': 1, 'FromTime1': '00:00', 'ToTime1': '14:00',
                    'Shift2': 2, 'FromTime2': '14:00', 'ToTime2': '22:00',
                    'Shift3': 3, 'FromTime3': '22:00', 'ToTime3': '00:00'
                }

    def load_data_to_IOSettings_dict(self):
        with self.SessionLocal() as session:
            try:
                io_entries = session.query(IOSettings).all()

                self.IOSettings_dict = {
                    entry.Key: {'Enable': entry.Enable, 'Value': entry.Value} for entry in io_entries
                }

                if not self.IOSettings_dict:
                    self.IOSettings_dict = {
                        'AUTO_SAVE_READING': {'Enable': '0', 'Value': None},
                        'BUZZER': {'Enable': '0', 'Value': 'Ok'},
                        'CYCLE_STOP_TIMER': {'Enable': '0', 'Value': '2'},
                        'MASTER_GROUPING': {'Enable': '0', 'Value': None},
                        'PART_TRACEABILITY': {'Enable': '0', 'Value': 'Manual Reset'},
                        'RELAY': {'Enable': '0', 'Value': '2'},
                        'TIME_TO_MASTER_SET': {'Enable': '0', 'Value': '2'},
                        'SAVE_MASTER_CALIBRATION': {'Enable': 'OFF', 'Value': None}
                    }
                return self.IOSettings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_IOSettings_dict: {e}")
                return { # Return defaults on error
                    'AUTO_SAVE_READING': {'Enable': '0', 'Value': None},
                    'BUZZER': {'Enable': '0', 'Value': 'Ok'},
                    'CYCLE_STOP_TIMER': {'Enable': '0', 'Value': '2'},
                    'MASTER_GROUPING': {'Enable': '0', 'Value': None},
                    'PART_TRACEABILITY': {'Enable': '0', 'Value': 'Manual Reset'},
                    'RELAY': {'Enable': '0', 'Value': '2'},
                    'TIME_TO_MASTER_SET': {'Enable': '0', 'Value': '2'},
                    'SAVE_MASTER_CALIBRATION': {'Enable': 'OFF', 'Value': None}
                }
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_IOSettings_dict: {e}")
                return { # Return defaults on error
                    'AUTO_SAVE_READING': {'Enable': '0', 'Value': None},
                    'BUZZER': {'Enable': '0', 'Value': 'Ok'},
                    'CYCLE_STOP_TIMER': {'Enable': '0', 'Value': '2'},
                    'MASTER_GROUPING': {'Enable': '0', 'Value': None},
                    'PART_TRACEABILITY': {'Enable': '0', 'Value': 'Manual Reset'},
                    'RELAY': {'Enable': '0', 'Value': '2'},
                    'TIME_TO_MASTER_SET': {'Enable': '0', 'Value': '2'},
                    'SAVE_MASTER_CALIBRATION': {'Enable': 'OFF', 'Value': None}
                }
                
    def load_data_to_AngleCalculationSettings_dict(self, program_id: int = None):
        """
        Load AngleCalculationSettings from DB for the given ProgramId.
        Returns a dictionary with string values (suitable for UI).
        If no data exists for the given ProgramId, returns default values.
        """
        with self.SessionLocal() as session:
            try:
                # Ensure program_id is an int for querying
                if program_id is not None:
                    program_id = int(program_id)

                # print(f"[DB] Loading AngleCalculationSettings for ProgramId={program_id}")

                # Fetch the entry from database
                angle_entry = (
                    session.query(AngleCalculationSettings)
                    .filter_by(ProgramId=program_id)
                    .first()
                )
                # print("angle entry.........",angle_entry)
                # If no entry found → return default values
                if not angle_entry:
                    # print(f"[DB] No AngleCalculationSettings found for ProgramId={program_id}. Using defaults.")
                    return {
                        'PROGRAM_ID': str(program_id) if program_id is not None else "0",
                        'ANGLE_CALCULATION_SETTINGS_ON_OFF': 'OFF',
                        'MASTER_ANGLE_DEGREES': '0',
                        'MASTER_ANGLE_MINUTES': '0',
                        'MASTER_ANGLE_SECONDS': '0',
                        'PLUS_TOLERANCE_MINUTES': '0',
                        'PLUS_TOLERANCE_SECONDS': '0',
                        'MINUS_TOLERANCE_MINUTES': '0',
                        'MINUS_TOLERANCE_SECONDS': '0',
                        'DISTANCE': '0.0',
                        'ANGLETYPE': 'Half Angle'
                    }

                # Otherwise → return actual data as strings for UI
                return {
                    'PROGRAM_ID': angle_entry.ProgramId,
                    'ANGLE_CALCULATION_SETTINGS_ON_OFF': angle_entry.Angle_Calculation_setting_on_off,
                    'MASTER_ANGLE_DEGREES': angle_entry.Master_angle_Degrees,
                    'MASTER_ANGLE_MINUTES': angle_entry.Master_angle_Minutes,
                    'MASTER_ANGLE_SECONDS': angle_entry.Master_angle_sec,
                    'PLUS_TOLERANCE_MINUTES': angle_entry.Plus_Tolerance_Minutes,
                    'PLUS_TOLERANCE_SECONDS': angle_entry.Plus_Tolerance_Seconds,
                    'MINUS_TOLERANCE_MINUTES': angle_entry.Minus_Tolerance_Minutes,
                    'MINUS_TOLERANCE_SECONDS': angle_entry.Minus_Tolerance_Seconds,
                    'DISTANCE': angle_entry.Distance,
                    'ANGLETYPE': angle_entry.AngleType,
                }

            except SQLAlchemyError as e:
                print(f"[DB] Database error during load_data_to_AngleCalculationSettings_dict: {e}")
                return {}
            except Exception as e:
                print(f"[DB] Unexpected error during load_data_to_AngleCalculationSettings_dict: {e}")
                return {}



    def load_data_to_AOCSettings_dict(self):
        with self.SessionLocal() as session:
            try:
                aoc_entries = session.query(AOCSettings).all()

                self.AOCSettings_dict = {entry.Key: entry.Value for entry in aoc_entries}

                if not self.AOCSettings_dict:
                    self.AOCSettings_dict = {
                        'AOC_ON_OFF': 'OFF',
                        'SPC_DATA_COUNT': '50'
                    }
                return self.AOCSettings_dict
            except SQLAlchemyError as e:
                print(f"Database error during load_data_to_AOCSettings_dict: {e}")
                return {'AOC_ON_OFF': 'OFF', 'SPC_DATA_COUNT': '50'}
            except Exception as e:
                print(f"An unexpected error occurred during load_data_to_AOCSettings_dict: {e}")
                return {'AOC_ON_OFF': 'OFF', 'SPC_DATA_COUNT': '50'}
            
    def load_data_to_ProgramSettings_dict(self, program_id: int):
        with self.SessionLocal() as session:
            try:
                # -------------------------------
                # 1️⃣ Program-level settings ONLY
                # -------------------------------
                program_dict = {
                    "ProgramSpecificSettings": {
                        "ProgramId": program_id,
                        "ProgramName": "",
                        "Mode": "Individual",
                        "Uom": "mm",
                        "AutoSave_Duration": 1.0,
                        "Responsiveness": 1
                    }
                }

                # -------------------------------
                # 2️⃣ Load ProgramSpecificSettings
                # -------------------------------
                prog = session.query(ProgramSettings)\
                            .filter_by(ProgramId=program_id)\
                            .first()

                if prog:
                    program_dict["ProgramSpecificSettings"].update({
                        "ProgramId": prog.ProgramId,
                        "ProgramName": prog.ProgramName,
                        "Mode": prog.Mode,
                        "Uom": prog.Uom,
                        "AutoSave_Duration": prog.AutoSave_Duration,
                        "Responsiveness": prog.Responsiveness
                    })

                # -------------------------------
                # 3️⃣ Load ProbeBasedSettings
                # -------------------------------
                probes = session.query(ProbeBasedSettings)\
                                .filter_by(ProgramId=program_id)\
                                .all()

                for probe in probes:
                    dim = str(probe.Dimension).strip().upper()
                    if not dim:
                        continue

                    if dim not in program_dict:
                        program_dict[dim] = {
                            "ProbeBasedSettings": {},
                            "AOCBasedSettings": {}
                        }

                    program_dict[dim]["ProbeBasedSettings"] = {
                        "Formula": probe.Formula,
                        "ProgramName": probe.ProgramName,
                        "DimensionName": probe.DimensionName,
                        "MasterType": probe.MasterType,
                        "MasterLower": probe.MasterLower,
                        "Master": probe.Master,
                        "MasterHigher": probe.MasterHigher,
                        # "UpperOffsetLimit": probe.UpperOffsetLimit,
                        "UpperSpecificationLimit": probe.UpperSpecificationLimit,
                        "UpperControlLimit": probe.UpperControlLimit,
                        "NominalValue": probe.NominalValue,
                        "LowerControlLimit": probe.LowerControlLimit,
                        "LowerSpecificationLimit": probe.LowerSpecificationLimit,
                        # "LowerOffsetLimit": probe.LowerOffsetLimit,
                        "Ovality": probe.Ovality,
                        "Range": probe.Range,
                        "Method": probe.Method,
                        "Case": probe.Case,
                        "CaseT": probe.CaseT,
                        "LeastCount":probe.LeastCount,
                        "ProbeSensitivity": probe.ProbeSensitivity,
                        "AirSensitivityQuotient": probe.AirSensitivityQuotient
                    }

                # -------------------------------
                # 4️⃣ Load AOCBasedSettings
                # -------------------------------
                aocs = session.query(AOCBasedSettings)\
                            .filter_by(ProgramId=program_id)\
                            .all()

                for aoc in aocs:
                    dim = str(aoc.Dimension).strip().upper()
                    if not dim or dim not in program_dict:
                        continue

                    program_dict[dim]["AOCBasedSettings"] = {
                        "Axis": aoc.Axis,
                        "OffsetNo": aoc.OffsetNo,
                        "UpperOffsetLimit": aoc.UpperOffsetLimit,
                        "LowerOffsetLimit": aoc.LowerOffsetLimit,
                        "Machine": aoc.Machine,
                        "Direction": aoc.Direction,
                        "TurretNo": aoc.TurretNo,
                        "BufferPartNo": aoc.BufferPartNo
                    }

                return program_dict

            except Exception as e:
                print(f"Error loading ProgramSettings_dict for program_id {program_id}: {e}")
                return {}

    
