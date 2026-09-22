from PySide2.QtCore import QObject, QTimer

class PageStatusManager(QObject):

    def __init__(self, label, stacked):
        try:
            super().__init__()

            self.label = label
            self.stacked = stacked

            self.page_index = None

            self.timer = QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.hide)

            self.label.setText("")

            # Make text bold
            font = self.label.font()
            font.setBold(True)
            self.label.setFont(font)
            self.fixed_messages = {}
            # Hide status when page changes
            self.stacked.currentChanged.connect(self.on_page_changed)
        except Exception as e:
            print(f"Error in init of PageStausManager - >{e}")

    # def show(self, page_index, message, timeout=2000):
    #     try:
    #         # print("STATUS:", page_index, message)
    #         self.page_index = page_index

    #         # Show only on correct page
    #         if self.stacked.currentIndex() != page_index:
    #             return

    #         self.timer.stop()

    #         self.label.setText(message)


    #         if timeout > 0:
    #             self.timer.start(timeout)
    #     except Exception as e:
    #         print(f"Error in show function of PageStausManager - >{e}")
    def show(self, page_index, message, timeout=2000, msg_type="info"):
        try:
            self.page_index = page_index

            if self.stacked.currentIndex() != page_index:
                return

            self.timer.stop()

            # Apply style based on message type
            self.apply_style(msg_type)

            self.label.setText(message)

            if timeout > 0:
                self.timer.start(timeout)

        except Exception as e:
            print(f"Error in show function of PageStatusManager -> {e}")
    def apply_style(self, msg_type):
        try:
            styles = {
            "success": "background-color: green; color: white;",
            "error": "background-color: red; color: white;",
            "warning": "background-color: #8B6508; color: white;",
            "info": "background-color: black; color: white;",
            }

            self.label.setStyleSheet(
                styles.get(msg_type, styles["info"])
            )

            

        except Exception as e:
            print(f"Error in apply_style -> {e}")
    
    def hide(self):
        try:
            self.timer.stop()

            self.label.clear()

            self.label.setStyleSheet("""
                QLabel {
                    background-color: black;
                }
            """)

        except Exception as e:
            print(f"Error in hide function -> {e}")
    # def hide(self):
    #     try:
    #         self.timer.stop()

    #         self.label.clear()
    #     except Exception as e:
    #         print(f"Error in hide function of PageStausManager - >{e}")
    def set_fixed_message(self, page_index, message,msg_type="info"):
        """
        Store a persistent message for a page.
        It will be shown whenever that page becomes active.
        """
        try:
            self.fixed_messages[page_index] = (message, msg_type)
            
            # If currently on that page, show immediately
            if self.stacked.currentIndex() == page_index:
                self.timer.stop()
                self.apply_style(msg_type)
                self.label.setText(message)

        except Exception as e:
            print(f"Error in set_fixed_message -> {e}")
    def on_page_changed(self, index):
        try:
            if index in self.fixed_messages:
                self.timer.stop()

                message, msg_type = self.fixed_messages[index]

                self.apply_style(msg_type)
                self.label.setText(message)
                return

            # No fixed message for this page
            self.hide()

        except Exception as e:
            print(f"Error in on_page_changed -> {e}")

        except Exception as e:
            print(f"Error in on_page_changed of PageStatusManager -> {e}")