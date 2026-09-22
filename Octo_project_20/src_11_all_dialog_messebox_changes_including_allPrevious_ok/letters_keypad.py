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
                ["Q","W","E","R","T","Y","U","I","O","P"],
                ["A","S","D","F","G","H","J","K","L"],
                ["Z","X","C","V","B","N","M"]
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



if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        win = Keyboard()
        win.show()
        sys.exit(app.exec_())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Application Error", str(e))

# from PySide2 import QtWidgets, QtCore, QtGui


# class Keyboard(QtWidgets.QWidget):
#     textEntered = QtCore.Signal(str)

#     def __init__(self, parent=None):
#         super().__init__(parent)

#         # ---------------- WINDOW SETUP ----------------
#         self.setWindowFlags(
#             QtCore.Qt.FramelessWindowHint |
#             QtCore.Qt.Tool |
#             QtCore.Qt.WindowStaysOnTopHint
#         )
#         self.setFixedSize(600, 370)
#         self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
#         self.setStyleSheet("background-color: #4a4a4a;")
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)


#         self.is_upper = True
#         self.show_symbols = False

#         # ---------------- KEY DEFINITIONS ----------------
#         self.letters = [
#             ["Q","W","E","R","T","Y","U","I","O","P"],
#             ["A","S","D","F","G","H","J","K","L"],
#             ["Z","X","C","V","B","N","M"]
#         ]

#         self.numbers = ["1","2","3","4","5","6","7","8","9","0"]
#         self.symbols = list('!@#$%^&*()_+-=[]{};:\'",.<>?/')

#         # ---------------- MAIN LAYOUT ----------------
#         self.main_layout = QtWidgets.QVBoxLayout(self)
#         self.main_layout.setContentsMargins(10, 10, 10, 10)
#         self.main_layout.setSpacing(8)

#         # ---------------- HEADER ----------------
#         header = QtWidgets.QHBoxLayout()
#         header.setAlignment(QtCore.Qt.AlignLeft)

#         title = QtWidgets.QLabel("Keyboard")
#         title.setStyleSheet("color:white; font-size:16px;")
#         header.addWidget(title)

#         header.addStretch()

#         close_btn = QtWidgets.QPushButton("X")
#         close_btn.setFixedSize(30, 30)
#         close_btn.setStyleSheet("""
#             QPushButton {
#                 background:#aa0000;
#                 color:white;
#                 border-radius:6px;
#             }
#             QPushButton:pressed {
#                 background:#cc0000;
#             }
#         """)
#         close_btn.clicked.connect(self.close_button)
#         header.addWidget(close_btn)

#         self.main_layout.addLayout(header)

#         # ---------------- INPUT BOX ----------------
#         self.input_box = QtWidgets.QLineEdit()
#         self.input_box.setFixedHeight(40)
#         self.input_box.setStyleSheet("""
#             QLineEdit {
#                 font: 16pt;
#                 color: white;
#                 background-color: #4a4a4a;
#                 border: 1px solid #777;
#                 border-radius: 6px;
#                 padding: 4px;
#             }
#         """)
#         self.main_layout.addWidget(self.input_box)

#         # ---------------- KEYBOARD AREA ----------------
#         self.keyboard_layout = QtWidgets.QVBoxLayout()
#         self.keyboard_layout.setSpacing(6)
#         self.keyboard_layout.setAlignment(QtCore.Qt.AlignCenter)
#         self.main_layout.addLayout(self.keyboard_layout)

#         # ---------------- EXTRA BUTTONS ----------------
#         self.extra_buttons_layout = QtWidgets.QHBoxLayout()
#         self.extra_buttons_layout.setSpacing(6)
#         self.extra_buttons_layout.setAlignment(QtCore.Qt.AlignCenter)
#         self.main_layout.addLayout(self.extra_buttons_layout)

#         self.create_keyboard()
#         self.create_extra_buttons()

#     # ------------------------------------------------
#     # CENTER KEYBOARD RELATIVE TO PARENT
#     # ------------------------------------------------
#     def showEvent(self, event):
#         if self.parent():
#             parent_geo = self.parent().geometry()
#             self.move(
#                 parent_geo.x() + (parent_geo.width() - self.width()) // 2,
#                 parent_geo.y() + parent_geo.height() - self.height() - 10
#             )
#         super().showEvent(event)

#     # ------------------------------------------------
#     # CREATE KEY ROWS
#     # ------------------------------------------------
#     def create_keyboard(self):
#         while self.keyboard_layout.count():
#             item = self.keyboard_layout.takeAt(0)
#             if item.layout():
#                 while item.layout().count():
#                     w = item.layout().takeAt(0).widget()
#                     if w:
#                         w.deleteLater()

#         rows = self.letters if not self.show_symbols else [
#             self.numbers,
#             self.symbols[:10],
#             self.symbols[10:20],
#             self.symbols[20:30]
#         ]

#         self.buttons = []

#         for row in rows:
#             h_layout = QtWidgets.QHBoxLayout()
#             h_layout.setSpacing(6)
#             h_layout.setAlignment(QtCore.Qt.AlignCenter)

#             for char in row:
#                 btn = QtWidgets.QPushButton(
#                     char.upper() if self.is_upper and not self.show_symbols else char
#                 )
#                 btn.setFixedSize(52, 52)
#                 btn.setSizePolicy(
#                     QtWidgets.QSizePolicy.Fixed,
#                     QtWidgets.QSizePolicy.Fixed
#                 )
#                 btn.setStyleSheet("""
#                     QPushButton {
#                         background-color: #6a6a6a;
#                         color: white;
#                         font: 15pt;
#                         border-radius: 8px;
#                     }
#                     QPushButton:pressed {
#                         background-color: #8a8a8a;
#                     }
#                 """)
#                 btn.clicked.connect(
#                     lambda _, c=char: self.input_box.setText(
#                         self.input_box.text() +
#                         (c.upper() if self.is_upper and not self.show_symbols else c)
#                     )
#                 )
#                 h_layout.addWidget(btn)
#                 self.buttons.append(btn)

#             self.keyboard_layout.addLayout(h_layout)

#     # ------------------------------------------------
#     # EXTRA BUTTONS (BOTTOM ROW)
#     # ------------------------------------------------
#     def create_extra_buttons(self):
#         while self.extra_buttons_layout.count():
#             w = self.extra_buttons_layout.takeAt(0).widget()
#             if w:
#                 w.deleteLater()

#         def mk_btn(text, w):
#             b = QtWidgets.QPushButton(text)
#             b.setFixedSize(w, 52)
#             b.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#             b.setStyleSheet("""
#                 QPushButton {
#                     background-color: #6a6a6a;
#                     color: white;
#                     font: 14pt;
#                     border-radius: 8px;
#                 }
#                 QPushButton:pressed {
#                     background-color: #8a8a8a;
#                 }
#             """)
#             return b

#         self.btn_space = mk_btn("Space", 180)
#         self.btn_space.clicked.connect(lambda: self.input_box.insert(" "))

#         self.btn_shift = mk_btn("ab/AB", 80)
#         self.btn_shift.clicked.connect(self.toggle_case)

#         self.btn_symbols = mk_btn("<>", 80)
#         self.btn_symbols.clicked.connect(self.toggle_symbols)

#         self.btn_back = mk_btn("<-", 70)
#         self.btn_back.clicked.connect(lambda: self.input_box.setText(self.input_box.text()[:-1]))

#         self.btn_clear = mk_btn("Clear", 80)
#         self.btn_clear.clicked.connect(self.input_box.clear)

#         self.btn_enter = mk_btn("Enter", 100)
#         self.btn_enter.clicked.connect(self.commit_text)

#         for b in [
#             self.btn_space, self.btn_shift, self.btn_symbols,
#             self.btn_back, self.btn_clear, self.btn_enter
#         ]:
#             self.extra_buttons_layout.addWidget(b)

#     # ------------------------------------------------
#     # LOGIC
#     # ------------------------------------------------
#     def toggle_case(self):
#         self.is_upper = not self.is_upper
#         if not self.show_symbols:
#             for btn in self.buttons:
#                 btn.setText(btn.text().upper() if self.is_upper else btn.text().lower())

#     def toggle_symbols(self):
#         self.show_symbols = not self.show_symbols
#         self.create_keyboard()
    
#     def close_button(self):
#         self.close()

#     def commit_text(self):
#         self.textEntered.emit(self.input_box.text())
#         self.input_box.clear()
#         self.close()
