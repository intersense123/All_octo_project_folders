from PySide2 import QtWidgets, QtCore, QtGui

class Keyboard(QtWidgets.QWidget):
    textEntered = QtCore.Signal(str)

    def __init__(self,parent=None):
        try:
            super().__init__(parent)
            self.showFullScreen()
            self.setWindowTitle("Mobile Keyboard")
            self.setFixedSize(600, 370)
            self.is_upper = True
            self.show_symbols = False
            
            self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

            # Define keys
            self.letters = [
                ["A","B","C","D","E","F","G","H","I","J"],
                ["K","L","M","N","O","P","Q","R","S"],
                ["T","U","V","W","X","Y","Z"]
            ]
            self.numbers = ["1","2","3","4","5","6","7","8","9","0"]
            self.symbols = list('!@#$%^*()_+-=[]{};:\'",.<>?/|`~')

            # Layouts
            self.main_layout = QtWidgets.QVBoxLayout(self)
            self.setStyleSheet("background-color: #4a4a4a;")  # Grey background
            
           
            # Header layout
            self.headerLayout = QtWidgets.QHBoxLayout()
            self.headerLayout.setContentsMargins(0, 0, 0, 10)

            self.headerLabel = QtWidgets.QLabel("Keyboard")
            self.headerLabel.setStyleSheet("color: white; font-size: 15px;")
            self.headerLayout.addWidget(self.headerLabel)

            self.closeButton = QtWidgets.QPushButton("X")
            self.closeButton.setFixedSize(30, 30)
            self.closeButton.setStyleSheet("background-color: #aa0000; color: white; font-size: 14px; border-radius: 5px;")
            self.closeButton.clicked.connect(self.commit_text)
            self.headerLayout.addWidget(self.closeButton)

            self.main_layout.addLayout(self.headerLayout)

            self.input_box = QtWidgets.QLineEdit()
            self.input_box.setMinimumHeight(40)
            self.input_box.setStyleSheet('font: 15pt "MS Shell Dlg 2"; color: white; background-color: #4a4a4a;')
            self.main_layout.addWidget(self.input_box)

            self.keyboard_layout = QtWidgets.QVBoxLayout()
            self.main_layout.addLayout(self.keyboard_layout)

            self.extra_buttons_layout = QtWidgets.QHBoxLayout()
            self.main_layout.addLayout(self.extra_buttons_layout)

            self.create_keyboard()
            self.create_extra_buttons()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Init Error", str(e))
            
    def showEvent(self, event):
        parent = self.parentWidget()
        if parent:
            geo = parent.rect()
            self.move(
                (geo.width() - self.width()) // 6,
                geo.height() - self.height() - 400
            )
        super().showEvent(event)



    def create_keyboard(self):
        try:
            # Clear previous
            for i in reversed(range(self.keyboard_layout.count())):
                item = self.keyboard_layout.itemAt(i)
                if item.layout():
                    while item.layout().count():
                        child = item.layout().takeAt(0)
                        if child.widget():
                            child.widget().deleteLater()
                    self.keyboard_layout.removeItem(item)

            # Determine layout
            if self.show_symbols:
                rows = [
                    self.numbers,
                    self.symbols[:10],
                    self.symbols[10:20],
                    self.symbols[20:30]
                ]
            else:
                rows = self.letters

            self.buttons = []

            for row in rows:
                h_layout = QtWidgets.QHBoxLayout()
                h_layout.setSpacing(5)
                for char in row:
                    btn = QtWidgets.QPushButton(char.upper() if self.is_upper and not self.show_symbols else char)
                    btn.setFixedSize(50, 50)
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #6a6a6a;
                            color: white;
                            font: 15pt "MS Shell Dlg 2";
                            border-radius: 8px;
                        }
                        QPushButton:pressed {
                            background-color: #8a8a8a;
                        }
                    """)
                    btn.clicked.connect(lambda checked=False, c=char: self.input_box.setText(
                        self.input_box.text() + (c.upper() if self.is_upper and not self.show_symbols else c)
                    ))
                    h_layout.addWidget(btn)
                    self.buttons.append(btn)
                self.keyboard_layout.addLayout(h_layout)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Keyboard Error", str(e))



    def create_extra_buttons(self):
        try:
            # Clear previous
            while self.extra_buttons_layout.count():
                child = self.extra_buttons_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            # Space
            self.btn_space = QtWidgets.QPushButton("Space")
            self.btn_space.setFixedSize(170, 50)
            self.btn_space.setStyleSheet("background-color: #6a6a6a; color: white; font: 15pt; border-radius: 8px;")
            self.btn_space.clicked.connect(lambda: self.input_box.setText(self.input_box.text() + " "))
            self.extra_buttons_layout.addWidget(self.btn_space)

            # Shift
            self.btn_shift = QtWidgets.QPushButton("ab/AB")
            self.btn_shift.setFixedSize(70, 50)
            self.btn_shift.setStyleSheet("background-color: #6a6a6a; color: white; font: 18pt; border-radius: 8px;")
            self.btn_shift.clicked.connect(self.toggle_case)
            self.extra_buttons_layout.addWidget(self.btn_shift)

            # Symbols
            self.btn_symbols = QtWidgets.QPushButton("<>")
            self.btn_symbols.setFixedSize(70, 50)
            self.btn_symbols.setStyleSheet("background-color: #6a6a6a; color: white; font: 18pt; border-radius: 8px;")
            self.btn_symbols.clicked.connect(self.toggle_symbols)
            self.extra_buttons_layout.addWidget(self.btn_symbols)

            # Backspace
            self.btn_back = QtWidgets.QPushButton("<-")
            self.btn_back.setFixedSize(70, 50)
            self.btn_back.setStyleSheet("background-color: #6a6a6a; color: white; font: 18pt; border-radius: 8px;")
            self.btn_back.clicked.connect(lambda: self.input_box.setText(self.input_box.text()[:-1]))
            self.extra_buttons_layout.addWidget(self.btn_back)

            # Clear
            self.btn_clear = QtWidgets.QPushButton("Clear")
            self.btn_clear.setFixedSize(70, 50)
            self.btn_clear.setStyleSheet("background-color: #6a6a6a; color: white; font: 18pt; border-radius: 8px;")
            self.btn_clear.clicked.connect(self.input_box.clear)
            self.extra_buttons_layout.addWidget(self.btn_clear)

            # Enter
            self.btn_Enter = QtWidgets.QPushButton("Enter")
            self.btn_Enter.setFixedSize(100, 50)
            self.btn_Enter.setStyleSheet("background-color: #6a6a6a; color: white; font: 18pt; border-radius: 8px;")
            self.btn_Enter.clicked.connect(self.commit_text)
            self.extra_buttons_layout.addWidget(self.btn_Enter)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Extra Buttons Error", str(e))

    def commit_text(self):
        try:
            self.textEntered.emit(self.input_box.text())
            self.input_box.clear()
            self.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Commit Text Error", str(e))

    def toggle_case(self):
        try:
            self.is_upper = not self.is_upper
            if not self.show_symbols:
                for btn in self.buttons:
                    btn.setText(btn.text().upper() if self.is_upper else btn.text().lower())
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Toggle Case Error", str(e))

    def toggle_symbols(self):
        try:
            self.show_symbols = not self.show_symbols
            self.create_keyboard()
            self.setFixedSize(self.width(), self.height())
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Toggle Symbols Error", str(e))

# class MainWindow(QtWidgets.QMainWindow):
#     def open_keyboard(self):
#         self.kb = Keyboard(parent=self)
#         self.kb.textEntered.connect(self.on_text)
#         self.kb.show()

#     def on_text(self, text):
#         print(text)


if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        win = Keyboard()
        win.show()
        sys.exit(app.exec_())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Application Error", str(e))
