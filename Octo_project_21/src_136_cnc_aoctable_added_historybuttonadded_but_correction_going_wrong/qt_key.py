from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

app = QApplication([])
w = QWidget()
layout = QVBoxLayout(w)

line = QLineEdit()
line.setPlaceholderText("Tap here, Qt keyboard should appear")
layout.addWidget(line)

w.show()
app.exec_()