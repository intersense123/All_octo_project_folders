import os
from messageBox import CustomMessageBox
import subprocess
class AboutPageHandler:
    def __init__(self, ui):
        try:
            # Initialize help page handler and load saved serial/model data
            self.ui = ui
            self.file_path = "/home/torizon/app/data/serial_model.txt"
               # Create file if it doesn't exist
            if not os.path.exists(self.file_path):
                with open(self.file_path, "w") as f:
                    pass   # creates an empty file
            self.load_modelSerialNumber()
            self.load_modelSerialNumber_toLabels()
            self.ui.button_update.clicked.connect(
                self.update_software_from_usb
            )
        except Exception as e:
            print(f"Error initializing AboutPageHandler: {e}")

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
            self.ui.status_manager.show(
                page_index=15,
                message="Data Loaded successfully.",
                timeout=0,
                msg_type="success"
            )
        except Exception as e:
            msg = CustomMessageBox("Failed to save model or serial number.", "error",
                                   parent=self.ui)
            msg.exec_()
            self.ui.status_manager.show(
                page_index=15,
                message="Please check inputs and try again.",
                timeout=0,
                msg_type="error"
            )

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

            # print("Model and Serial Number loaded successfully.")

        except Exception as e:
            print(f"Error loading model/serial number: {e}")
    
    # -----------------------------------
    # LOAD MODEL + SERIAL NUMBER TO LABELS
    # -----------------------------------
    def load_modelSerialNumber_toLabels(self):
        try:
            file_path = "/home/torizon/app/data/serial_model.txt"

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

            # print("Model and Serial Number loaded to labels successfully.")
            
        except Exception as e:
            print(f"Error loading labels: {e}")      
    import os

    def get_app_image(self,compose_path):
        """
        Returns image under app: service
        Example:
            intersense123/octo:1.2
        """
        try:
            # Parse compose file and return the image tag for the app service
            found_app = False

            with open(compose_path, "r") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped == "app:":
                        found_app = True
                        continue

                    if found_app and stripped.startswith("image:"):
                        return stripped.split("image:")[1].strip()
        except Exception as e:
            print(f"Error reading compose file {compose_path}: {e}")
        return None


    def update_software_from_usb(self):

        try:

            # -------------------------------------------------
            # CHECK USB DETECTED
            # -------------------------------------------------
            usb_found = False

            for item in os.listdir("/media"):
                usb_path = os.path.join("/media", item)

                if os.path.isdir(usb_path):
                    usb_found = True
                    break

            if not usb_found:
                msg = CustomMessageBox(
                    "USB device not detected.",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            usb_compose = None

            for item in os.listdir("/media"):

                usb_path = os.path.join("/media", item)

                if not os.path.isdir(usb_path):
                    continue

                compose = os.path.join(usb_path, "docker-compose.yml")
                compose_yaml = os.path.join(usb_path, "docker-compose.yaml")

                if os.path.isfile(compose):
                    usb_compose = compose
                    break

                if os.path.isfile(compose_yaml):
                    usb_compose = compose_yaml
                    break

            if usb_compose is None:

                msg = CustomMessageBox(
                    "Software not found in USB.",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            # -------------------------------------------------
            # READ HOST COMPOSE
            # -------------------------------------------------

            host_compose = "/home/torizon/docker-compose.yml"

            if not os.path.isfile(host_compose):

                msg = CustomMessageBox(
                    "Host docker-compose.yml not found.",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            # -------------------------------------------------
            # GET APP IMAGES
            # -------------------------------------------------

            current_image = self.get_app_image(host_compose)
            new_image = self.get_app_image(usb_compose)

            if current_image is None or new_image is None:

                msg = CustomMessageBox(
                    "Wrong application Found.",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            print("Current :", current_image)
            print("New     :", new_image)

            # -------------------------------------------------
            # SPLIT IMAGE
            # -------------------------------------------------

            current_name, current_tag = current_image.rsplit(":", 1)
            new_name, new_tag = new_image.rsplit(":", 1)

            # -------------------------------------------------
            # VALIDATION
            # -------------------------------------------------

            if current_name != new_name:

                msg = CustomMessageBox(
                    "Invalid update package detected.",
                    "error",
                    parent=self.ui
                )
                msg.exec_()
                return

            if current_tag == new_tag:

                msg = CustomMessageBox(
                    "Software version already installed.",
                    "warning",
                    parent=self.ui
                )
                msg.exec_()
                return

            # -------------------------------------------------
            # START UPDATE
            # -------------------------------------------------

            open("/tmp/start_update", "w").close()

            msg = CustomMessageBox(
                f"Updating software\n\nVersion {current_tag} → {new_tag}\n\nSystem will reboot automatically.",
                "success",
                parent=self.ui
            )
            msg.exec_()

        except Exception as e:

            print(e)

            msg = CustomMessageBox(
                "Unexpected update error occurred.",
                "error",
                parent=self.ui
            )
            msg.exec_()            
    # def update_software_from_usb(self):
    #     try:

    #         # -------------------------------------------------
    #         # CHECK USB DETECTED
    #         # -------------------------------------------------
    #         usb_found = False

    #         for item in os.listdir("/media"):
    #             usb_path = os.path.join("/media", item)

    #             if os.path.isdir(usb_path):
    #                 usb_found = True
    #                 break

    #         if not usb_found:
    #             msg = CustomMessageBox(
    #                 "USB device not detected.",
    #                 "error",
    #                 parent=self.ui
    #             )
    #             msg.exec_()
    #             return

    #         # -------------------------------------------------
    #         # RUN UPDATE SCRIPT
    #         # -------------------------------------------------
    #         result = subprocess.run(
    #             ["/bin/bash", "/home/torizon/app/update.sh"],
    #             capture_output=True,
    #             text=True
    #         )

    #         output = result.stdout + result.stderr

    #         print(output)

    #         # -------------------------------------------------
    #         # ERROR POPUPS
    #         # -------------------------------------------------

    #         if "No docker-compose.yml found in USB" in output:
    #             msg = CustomMessageBox(
    #                 "Software not found in USB.",
    #                 "error",
    #                 parent=self.ui
    #             )
    #             msg.exec_()
    #             return

    #         if "Same app version already installed" in output:
    #             msg = CustomMessageBox(
    #                 "Software version already installed.",
    #                 "warning",
    #                 parent=self.ui
    #             )
    #             msg.exec_()
    #             return

    #         if "Different app image detected" in output:
    #             msg = CustomMessageBox(
    #                 "Invalid update package detected.",
    #                 "error",
    #                 parent=self.ui
    #             )
    #             msg.exec_()
    #             return

    #         if "Weston container not running" in output:
    #             msg = CustomMessageBox(
    #                 "Weston container failed to start.",
    #                 "error",
    #                 parent=self.ui
    #             )
    #             msg.exec_()
    #             return

    #         if result.returncode != 0:
    #             msg = CustomMessageBox(
    #                 "Software update failed.",
    #                 "error",
    #                 parent=self.ui
    #             )
    #             msg.exec_()
    #             return

    #         # -------------------------------------------------
    #         # SUCCESS
    #         # -------------------------------------------------
    #         msg = CustomMessageBox(
    #             "Software update successful. System rebooting...",
    #             "success",
    #             parent=self.ui
    #         )
    #         msg.exec_()

    #     except Exception as e:
    #         print(f"Update error: {e}")

    #         msg = CustomMessageBox(
    #             "Unexpected update error occurred.",
    #             "error",
    #             parent=self.ui
    #         )
    #         msg.exec_()