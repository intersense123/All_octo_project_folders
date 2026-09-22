import os


class SerialModelManager:
    def __init__(self, ui):
        self.ui = ui
        self.file_path = "/home/torizon/app/serial_model.txt"

    # -----------------------------------
    # SAVE MODEL + SERIAL NUMBER
    # -----------------------------------
    def save_modelSerialNumber(self):
        try:
            model_no = self.ui.lineEdit_modelNo.text().strip()
            serial_no = self.ui.lineEdit_serialNo.text().strip()

            # "w" mode overwrites file (updates, not append)
            with open(self.file_path, "w") as file:
                file.write(f"{model_no}\n")
                file.write(f"{serial_no}\n")

            print("Model and Serial Number saved successfully.")

        except Exception as e:
            print(f"Error saving model/serial number: {e}")

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
            
            
            