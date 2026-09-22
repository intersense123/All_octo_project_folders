from PySide2 import QtWidgets, QtCore, QtGui

class Keyboard(QtWidgets.QWidget):
    textEntered = QtCore.Signal(str)
    keyboardClosed = QtCore.Signal() 

    def __init__(self,target_lineedit=None,parent=None):
        try:
            super().__init__(parent)
            # self.showFullScreen()
            # self.setWindowFlags(QtCore.Qt.Tool)
            self.setWindowTitle("Mobile Keyboard")
            self.setFixedSize(600, 370)
            self.is_upper = True
            self.show_symbols = False
            self.target_lineedit = target_lineedit
            
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
            self.main_layout.setContentsMargins(10, 10, 10, 10)
            self.main_layout.setSpacing(8)
            self.setStyleSheet("background-color: black;border: 1px solid grey;")  # Grey background
            
           
            # Header layout
            self.headerLayout = QtWidgets.QHBoxLayout()
            self.headerLayout.setContentsMargins(0, 0, 0, 10)

            self.headerLabel = QtWidgets.QLabel("Keyboard")
            self.headerLabel.setStyleSheet("color: white; font-size: 15px;")
            self.headerLayout.addWidget(self.headerLabel)

            self.closeButton = QtWidgets.QPushButton("X")
            self.closeButton.setFixedSize(30, 30)
            self.closeButton.setStyleSheet("background-color: #aa0000; color: white; font-size: 14px; border-radius: 5px;")
            self.closeButton.clicked.connect(self.handle_close)
            self.headerLayout.addWidget(self.closeButton)

            self.main_layout.addLayout(self.headerLayout)

            self.input_box = QtWidgets.QLineEdit()
            self.input_box.setMinimumHeight(40)
            self.input_box.setStyleSheet('font: 15pt "MS Shell Dlg 2"; color: white; background-color: #4a4a4a;')
            self.main_layout.addWidget(self.input_box)
            
            

            # if self.target_lineedit:
            #     self.input_box.setText(self.target_lineedit.text())

            self.keyboard_layout = QtWidgets.QVBoxLayout()
            self.keyboard_layout.setSpacing(6)
            self.keyboard_layout.setAlignment(QtCore.Qt.AlignCenter)
            self.main_layout.addLayout(self.keyboard_layout)

            self.extra_buttons_layout = QtWidgets.QHBoxLayout()
            self.extra_buttons_layout.setSpacing(6)
            self.extra_buttons_layout.setAlignment(QtCore.Qt.AlignCenter)
            self.main_layout.addLayout(self.extra_buttons_layout)

            self.create_keyboard()
            self.create_extra_buttons()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Init Error", str(e))
    # def handle_close(self):
    #     try:
    #         # same behavior as ENTER (like numpad)
    #         self.textEntered.emit(self.input_box.text())
    #         self.input_box.clear()
    #         self.keyboardClosed.emit()
    #         self.close()
    #     except Exception as e:
    #         print(f"Close error: {e}")
    def handle_close(self):
        self.keyboardClosed.emit()
        self.close()   # or close() if you prefer 
    # def showEvent(self, event):
    #     parent = self.parentWidget()
    #     if parent:
    #         geo = parent.rect()
    #         self.move(
    #             (geo.width() - self.width()) // 6,
    #             geo.height() - self.height() - 400
    #         )
    #     super().showEvent(event)
    def showEvent(self, event):
        parent = self.parentWidget()
        if parent:
            parent_pos = parent.mapToGlobal(QtCore.QPoint(0, 0))

            self.move(
                parent_pos.x() + (parent.width() - self.width()) // 2,
                parent_pos.y() + parent.height() - self.height() - 50
            )

        super().showEvent(event)


    # ------------------------------------------------
    # CREATE KEY ROWS
    # ------------------------------------------------
    def create_keyboard(self):
        while self.keyboard_layout.count():
            item = self.keyboard_layout.takeAt(0)
            if item.layout():
                while item.layout().count():
                    w = item.layout().takeAt(0).widget()
                    if w:
                        w.deleteLater()

        rows = self.letters if not self.show_symbols else [
            self.numbers,
            self.symbols[:10],
            self.symbols[10:20],
            self.symbols[20:30]
        ]

        self.buttons = []

        for row in rows:
            h_layout = QtWidgets.QHBoxLayout()
            h_layout.setSpacing(6)
            h_layout.setAlignment(QtCore.Qt.AlignCenter)

            for char in row:
                btn = QtWidgets.QPushButton(
                    char.upper() if self.is_upper and not self.show_symbols else char
                )
                btn.setFixedSize(52, 52)
                btn.setSizePolicy(
                    QtWidgets.QSizePolicy.Fixed,
                    QtWidgets.QSizePolicy.Fixed
                )
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #6a6a6a;
                        color: white;
                        font: 15pt;
                        border-radius: 8px;
                    }
                    QPushButton:pressed {
                        background-color: #8a8a8a;
                    }
                """)
                # btn.clicked.connect(lambda checked=False, c=char: self.input_box.setText(
                #         self.input_box.text() + (c.upper() if self.is_upper and not self.show_symbols else c)
                #     ))
                btn.clicked.connect(lambda checked=False, b=btn: 
                    self.input_box.insert(b.text())
                )
                h_layout.addWidget(btn)
                self.buttons.append(btn)

            self.keyboard_layout.addLayout(h_layout)

    def create_extra_buttons(self):
        while self.extra_buttons_layout.count():
            w = self.extra_buttons_layout.takeAt(0).widget()
            if w:
                w.deleteLater()

        def mk_btn(text, w):
            b = QtWidgets.QPushButton(text)
            b.setFixedSize(w, 52)
            b.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            b.setStyleSheet("""
                QPushButton {
                    background-color: #6a6a6a;
                    color: white;
                    font: 14pt;
                    border-radius: 8px;
                }
                QPushButton:pressed {
                    background-color: #8a8a8a;
                }
            """)
            return b

        self.btn_space = mk_btn("Space", 100)
        self.btn_space.clicked.connect(lambda: self.input_box.insert(" "))

        self.btn_shift = mk_btn("ab/AB", 60)
        self.btn_shift.clicked.connect(self.toggle_case)

        self.btn_symbols = mk_btn("<>", 60)
        self.btn_symbols.clicked.connect(self.toggle_symbols)

        self.btn_back = mk_btn("<-", 60)
        self.btn_back.clicked.connect(lambda: self.input_box.setText(self.input_box.text()[:-1]))

        self.btn_clear = mk_btn("Clear", 80)
        self.btn_clear.clicked.connect(self.input_box.clear)

        self.btn_enter = mk_btn("Enter", 100)
        self.btn_enter.clicked.connect(self.commit_text)

        for b in [
            self.btn_space, self.btn_shift, self.btn_symbols,
            self.btn_back, self.btn_clear, self.btn_enter
        ]:
            self.extra_buttons_layout.addWidget(b)
            

    # def close_clicked(self):
    #     try:
    #         if self.target_lineedit:
    #             self.target_lineedit.setText(self.Input_box.text())
    #             self.target_lineedit.parentWidget().setFocus()

    #         # ❌ REMOVE THIS LINE
    #         # self.Input_box.clear()

    #         self.close() # self.hide() if you want full close
    #         self.numpadClosed.emit()

    #     except Exception as e:
    #         QtWidgets.QMessageBox.critical(self, "Submit Error", str(e))

    def commit_text(self):
        try:
            if self.target_lineedit:
                self.target_lineedit.setText(self.input_box.text())
                self.target_lineedit.parentWidget().setFocus()
                
            # self.textEntered.emit(self.input_box.text())
            # self.input_box.clear()
            self.keyboardClosed.emit() 
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

