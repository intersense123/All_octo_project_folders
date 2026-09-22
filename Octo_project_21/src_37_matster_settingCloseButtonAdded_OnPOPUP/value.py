# To Handle All Of Values Regarding Application
class Value:
    def __init__(self):
        try:
            self.init_all_dictionaries()
        except Exception as e:
            print(f"Error during Value class initialization: {e}")
            # Initialize with empty dictionaries to prevent further errors
            self.ProgramSettings_dict = {}
            self.AngleCalculationSettings_dict = {}
            self.CNCList_dict = {} # Assuming this will be used
            self.IOSettings_dict = {}
            self.IPSettings_dict = {}
            self.NetworkedDatabaseSettings_dict = {}
            self.RS232Settings_dict = {}
            self.ShiftTimings_dict = {}
            self.UserManagment_dict = {}
            self.WifiSettings_dict = {}
            self.AOCSettings_dict = {}
            self.activeVariables_dict = {}
            # self.FactoryConfigSettings_dict = {}

    def init_all_dictionaries(self):
        try:
            self.init_mainProgramSettings_dictionary()
            self.init_AngleCalculationSettings_dictionary()
            self.init_CNCList_dictionary()
            self.init_IOSettings_dictionary()
            self.init_IPSettings_dictionary()
            self.init_NetworkedDatabaseSettings_dictionary()
            self.init_RS232Settings_dictionary()
            self.init_ShiftTimings_dictionary()
            self.init_UserManagment_dictionary()
            self.init_WifiSettings_dictionary()
            self.init_AOCsettings_dictionary()
            self.init_activeVariables_dictionary() # Ensure this is called
            # self.init_FactoryConfigSettings_dict()
        except Exception as e:
            print(f"Error initializing all dictionaries: {e}")
            raise # Re-raise to indicate a critical failure in setup

    def init_activeVariables_dictionary(self):
        try:
            self.activeVariables_dict = {
                'ActiveProgramId': 1,
                'AUTO_SAVE_READING': {'Enable': '0'},
                'BUZZER': {'Enable': '0'},
                'CYCLE_STOP_TIMER': {'Enable': '0'},
                'MASTER_GROUPING': {'Enable': '0'},
                'PART_TRACEABILITY': {'Enable': '0'},
                'RELAY': {'Enable': '0'},
                'TIME_TO_MASTER_SET': {'Enable': '0'},
                'AOCOnOff': 'OFF',
                'AngleCalculationOnOff' : 'OFF',
                'NetworkedDatabaseSettingsOnOff' : 'OFF',
                'RS232OnOff' : 'OFF'
            }
        except Exception as e:
            print(f"Error initializing activeVariables_dict: {e}")
            self.activeVariables_dict = {}
            
    def init_mainProgramSettings_dictionary(self):
        self.ProgramSettings_dict = {
            "ProgramSpecificSettings": {
                "ProgramId": 1,
                "ProgramName": "",
                "Mode": "Individual",
                "Uom": "mm",
                "AutoSave_Duration": 1.0
            }
        }

        for i in range(1, 9):
            self.ProgramSettings_dict[f"D{i}"] = {
                "ProbeBasedSettings": {},
                "AOCBasedSettings": {}
            }


    def init_CNCList_dictionary(self):
        try:
            self.CNCList_dict = {} # This dictionary is typically populated from the database
        except Exception as e:
            print(f"Error initializing CNCList_dict: {e}")
            self.CNCList_dict = {}

    def init_IOSettings_dictionary(self):
        try:
            self.IOSettings_dict = {
                    'AUTO_SAVE_READING': {'Enable': '0', 'Value': None},
                    'BUZZER': {'Enable': '0', 'Value': 'Ok'},
                    'CYCLE_STOP_TIMER': {'Enable': '0', 'Value': '2'},
                    'MASTER_GROUPING': {'Enable': '0', 'Value': None},
                    'PART_TRACEABILITY': {'Enable': '0', 'Value': 'Manual Reset'},
                    'RELAY': {'Enable': '0', 'Value': '2'},
                    'TIME_TO_MASTER_SET': {'Enable': '0', 'Value': '2'}
                }
        except Exception as e:
            print(f"Error initializing IOSettings_dict: {e}")
            self.IOSettings_dict = {}

    def init_AngleCalculationSettings_dictionary(self):
        try:
            self.AngleCalculationSettings_dict = {
                    'PROGRAM_ID': 1,
                    'ANGLE_CALCULATION_SETTINGS_ON_OFF': 'OFF',
                    'MASTER_ANGLE_DEGREES': 0,
                    'MASTER_ANGLE_MINUTES': 0,
                    'MASTER_ANGLE_SECONDS': 0,
                    'PLUS_TOLERANCE_MINUTES': 0,
                    'PLUS_TOLERANCE_SECONDS': 0,
                    'MINUS_TOLERANCE_MINUTES': 0,
                    'MINUS_TOLERANCE_SECONDS': 0,
                    'DISTANCE': 0.0,
                    'ANGLETYPE': 'Half Angle'
                }
        except Exception as e:
            print(f"Error initializing AngleCalculationSettings_dict: {e}")
            self.AngleCalculationSettings_dict = {}
        
    def init_IPSettings_dictionary(self):
        try:
            self.IPSettings_dict = {
                    'SelfIPAddress': '',
                    'SubnetMask': '',
                    'DefaultGateway':'' 
                }
        except Exception as e:
            print(f"Error initializing IPSettings_dict: {e}")
            self.IPSettings_dict = {}

    def init_NetworkedDatabaseSettings_dictionary(self):
        try:
            self.NetworkedDatabaseSettings_dict = {
                    'NETWORKE_BASED_DATABASE_ON_OFF': 'OFF',
                    'MS_SQL_DRIVER_NAME': '{SQL Server Native Client 11.0}',
                    'MS_SQL_SERVER_NAME': 'LENOVOCI5\\SQLEXPRESS',
                    'MS_SQL_DATABASE_NAME': 'Octo_PreciGo',
                    'MS_SQL_USERNAME': 'sa',
                    'MS_SQL_PASSWORD': 'password'
                }
        except Exception as e:
            print(f"Error initializing NetworkedDatabaseSettings_dict: {e}")
            self.NetworkedDatabaseSettings_dict = {}

    def init_RS232Settings_dictionary(self):
        try:
            self.RS232Settings_dict = {
                    'RS232_ON_OFF': 'OFF',
                    'BAUD_RATE': '115200',
                    'DATA_BITS': '8',
                    'PARITY': 'None',
                    'STOP_BITS': 'One',
                    'FLOW_CONTROL': 'None',
                    'PORT_NAME': 'ttymxc0'
                }
        except Exception as e:
            print(f"Error initializing RS232Settings_dict: {e}")
            self.RS232Settings_dict = {}

    def init_ShiftTimings_dictionary(self):
        try:
            self.ShiftTimings_dict = {
                    'Shift1': 1,
                    'FromTime1': '00:00',
                    'ToTime1': '14:00',
                
                    'Shift2': 2,
                    'FromTime2': '14:00',
                    'ToTime2': '22:00',
                
                    'Shift3': 3,
                    'FromTime3': '22:00',
                    'ToTime3': '00:00'
                }
        except Exception as e:
            print(f"Error initializing ShiftTimings_dict: {e}")
            self.ShiftTimings_dict = {}

    def init_UserManagment_dictionary(self):
        try:
            self.UserManagment_dict = {
                    'Username' : 'user',
                    'Password' : 'password',
                    'AccessType' : 1
                }
        except Exception as e:
            print(f"Error initializing UserManagment_dict: {e}")
            self.UserManagment_dict = {}

    def init_WifiSettings_dictionary(self):
        try:
            self.WifiSettings_dict = {
                    'WifiSSID': '',
                    'WifiPassword': ''
                }
        except Exception as e:
            print(f"Error initializing WifiSettings_dict: {e}")
            self.WifiSettings_dict = {}

    def init_AOCsettings_dictionary(self):
        try:
            self.AOCSettings_dict = {
                    'AOC_ON_OFF': 'OFF',
                    'SPC_DATA_COUNT': '50'
                }
        except Exception as e:
            print(f"Error initializing AOCSettings_dict: {e}")
            self.AOCSettings_dict = {}
            