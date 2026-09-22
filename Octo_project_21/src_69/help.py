import os
from messageBox import CustomMessageBox

class SerialModelManager:
    def __init__(self, ui):
        self.ui = ui
        self.file_path = "/home/torizon/app/serial_model.txt"
        self.load_modelSerialNumber()
        self.load_modelSerialNumber_toLabels()  

    # -----------------------------------
    # SAVE MODEL + SERIAL NUMBER
    # -----------------------------------
    def save_modelSerialNumber(self):
        try:
            model_no = self.ui.lineEdit_modelNo.text().strip()
            serial_no = self.ui.lineEdit_serialNo.text().strip()
            # Check empty fields
            if not model_no or not serial_no:
                raise ValueError("Fields cannot be empty")
            # "w" mode overwrites file (updates, not append)
            with open(self.file_path, "w") as file:
                file.write(f"{model_no}\n")
                file.write(f"{serial_no}\n")

            self.load_modelSerialNumber_toLabels() 
            msg = CustomMessageBox("Model and Serial Number saved successfully.", "success",
                                   parent=self.ui)
            msg.exec_() 
        except Exception as e:
            msg = CustomMessageBox("Failed to save model or serial number.", "error",
                                   parent=self.ui)
            msg.exec_()

    # -----------------------------------
    # LOAD MODEL + SERIAL NUMBER
    # -----------------------------------
    def load_modelSerialNumber(self):
        try:
            # Check file exists
            if not os.path.exists(self.file_path):
                print("serial_model.txt not found.")
                return

            with open(self.file_path, "r") as file:
                lines = file.readlines()

            # Remove newline characters
            lines = [line.strip() for line in lines]

            # Load into line edits
            if len(lines) >= 1:
                self.ui.lineEdit_modelNo.setText(lines[0])

            if len(lines) >= 2:
                self.ui.lineEdit_serialNo.setText(lines[1])

            print("Model and Serial Number loaded successfully.")

        except Exception as e:
            print(f"Error loading model/serial number: {e}")
    
    # -----------------------------------
    # LOAD MODEL + SERIAL NUMBER TO LABELS
    # -----------------------------------
    def load_modelSerialNumber_toLabels(self):
        try:
            file_path = "/home/torizon/app/serial_model.txt"

            # Check file exists
            if not os.path.exists(file_path):
                print("serial_model.txt not found.")
                return

            # Read file
            with open(file_path, "r") as file:
                lines = file.readlines()

            # Remove newline spaces
            lines = [line.strip() for line in lines]

            # First line -> Model Number
            if len(lines) >= 1:
                self.ui.label_ModelNumber.setText(lines[0])

            # Second line -> Serial Number
            if len(lines) >= 2:
                self.ui.label_SerialNumber.setText(lines[1])

            print("Model and Serial Number loaded to labels successfully.")

        except Exception as e:
            print(f"Error loading labels: {e}")      
                
                