from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel,QSizePolicy,
    QVBoxLayout, QWidget)
from PySide6.QtCore import QTimer
import sys
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set object name if not already set
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            

        # Initial window size
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(u"QLabel{\n"
"	 font-size: 16pt;\n"
"     min-height:30px;\n"
"}")

        # Central widget of QMainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Main container widget
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 781, 501))

        # MAIN VERTICAL LAYOUT (controls HEIGHT of rows)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # ================= FIRST ROW =================
        # Horizontal layout → holds D1 and D2
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        # -------- Left container (D1) --------
        self.verticalLayout_2_container = QWidget(self.widget)
        self.verticalLayout_2_container.setObjectName("verticalLayout_2_container")

        # Vertical layout inside left container
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayout_2_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Add left container to first-row horizontal layout
        self.horizontalLayout.addWidget(self.verticalLayout_2_container)
        

        # -------- Right container (D2) --------
        self.verticalLayout_3_container = QWidget(self.widget)
        self.verticalLayout_3_container.setObjectName("verticalLayout_3_container")

        # Vertical layout inside right container
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayout_3_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        # Add right container to first-row horizontal layout
        self.horizontalLayout.addWidget(self.verticalLayout_3_container)

        # Add FIRST ROW to MAIN vertical layout
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # ================= SECOND ROW =================
        # Horizontal layout → holds D3 and D4
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        # -------- Bottom-left container (D3) --------
        self.verticalLayout_4_container = QWidget(self.widget)
        self.verticalLayout_4_container.setObjectName("verticalLayout_4_container")

        self.verticalLayout_4 = QVBoxLayout(self.verticalLayout_4_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_2.addWidget(self.verticalLayout_4_container)

        # -------- Bottom-right container (D4) --------
        self.verticalLayout_5_container = QWidget(self.widget)
        self.verticalLayout_5_container.setObjectName("verticalLayout_5_container")

        self.verticalLayout_5 = QVBoxLayout(self.verticalLayout_5_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_2.addWidget(self.verticalLayout_5_container)

        # Add SECOND ROW to MAIN vertical layout
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
   
class SPCBase:
    """
    Base class for one SPC chart (D1–D4).
    Handles:
    - scaling values
    - background zones
    - plotting data
    """

    def __init__(self, title, limits):
        try:
            self.title = title                  # Graph title (D1, D2, ...)
            self.limits = limits                # SPC limits

            self.data_raw = []                  # Raw input values
            self.data_scaled = []               # Scaled values for plotting

            self.y_positions = np.arange(7)     # 7 SPC zones

            # Colors and styles for limit lines
            self.line_colors = ["red","red","yellow","green","yellow","red","red"]
            self.line_styles = ["-","--",":","-.",":","--","-"]

            # Create matplotlib figure and canvas
            self.fig = Figure(figsize=(4.5, 2.2))
            self.canvas = FigureCanvas(self.fig)
            self.ax = self.fig.add_subplot(111)

            # Dark theme
            self.fig.patch.set_facecolor("black")
            self.ax.tick_params(axis="x", colors="white")
            self.ax.tick_params(axis="y", colors="white")

            # Draw empty graph initially
            self.init_blank_ui()
        except Exception as e:
            print(f"Error in SPC Base class initialization :{e}")   
            
    def _scale_value(self, v):
        for i in range(6):
            low = self.limits[i]
            high = self.limits[i + 1]

            if low <= v <= high or high <= v <= low:
                return i + (v - low) / (high - low)

        return 0 if v < self.limits[0] else 6

    def _draw_background(self):
        self.ax.axhspan(0, 1, color="red", alpha=0.8)
        self.ax.axhspan(1, 2, color="yellow", alpha=0.8)
        self.ax.axhspan(2, 4, color="green", alpha=0.8)
        self.ax.axhspan(4, 5, color="yellow", alpha=0.8)
        self.ax.axhspan(5, 6, color="red", alpha=0.8)

    def _draw_limit_lines(self):
        try:
            xmax = len(self.data_raw) if self.data_raw else 1
            for i in range(7):
                self.ax.hlines(
                    self.y_positions[i],
                    xmin=0,
                    xmax=xmax,
                    colors=self.line_colors[i],
                    linestyles=self.line_styles[i],
                    linewidth=1.2
                )
        except Exception as e:
            print("Error in draw_limit_lines -> {e}")

    def init_blank_ui(self):
        try:
            """
            Draw empty SPC chart without data points.
            Called once at startup.
            """

            self.ax.clear()
            self._draw_background()
            self._draw_limit_lines()

            self.ax.set_ylim(-0.5, 6.5)
            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white")
            self.ax.set_xlabel("Job Count")
            self.ax.set_ylabel(self.title)

            self.canvas.draw_idle()
        except Exception as e:
            print(f"Error in init_blank_ui -> {e}")
    
    def generate_graph(self, raw_data):
        try:
            self.data_raw = raw_data
            self.data_scaled = [self._scale_value(v) for v in raw_data]

            self.ax.clear()
            self._draw_background()
            self._draw_limit_lines()

            x = np.arange(1, len(self.data_scaled) + 1)
            self.ax.plot(x, self.data_scaled, "bo-", markersize=3)

            self.ax.set_ylim(-0.5, 6.5)
            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_xlabel("Job Count")
            self.ax.set_ylabel(self.title)

            self.canvas.draw_idle()
        except Exception as e:
            print("Erro in gnerate_graph -> {e}")
    
    def update_graph(self, value):
        try:
            self.data_raw.append(value)

            if len(self.data_raw) > 20:
                self.data_raw.pop(0)

            scaled = [self._scale_value(v) for v in self.data_raw]

            self.ax.clear()
            self._draw_background()
            self._draw_limit_lines()

            x = np.arange(1, len(scaled) + 1)
            self.ax.plot(x, scaled, "bo-", markersize=3)

            self.ax.set_ylim(-0.5, 6.5)
            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white")
            self.canvas.draw_idle()
        except Exception as e:
            print(f"Error in update_graph -> {e}")
         
class SPC_D1(SPCBase):
    """
    SPC class for Dimension 1
    """
    def __init__(self):
        super().__init__("D1", [10, 25, 50, 55, 60, 70, 150])
        
class SPC_D2(SPCBase):
    """
    SPC class for Dimension 2
    """
    def __init__(self):
        super().__init__("D2", [5, 15, 30, 35, 40, 50, 90])
        
class SPC_D3(SPCBase):
    """
    SPC class for Dimension 3
    """
    def __init__(self):
        super().__init__("D3", [100, 120, 140, 150, 160, 170, 200])
        
class SPC_D4(SPCBase):
    """
    SPC class for Dimension 4
    """
    def __init__(self):
        super().__init__("D4", [1, 2, 3, 3.5, 4, 5, 6])
    
class SPCWidget(QWidget):
    def __init__(self, spc, parent=None):
        super().__init__(parent)
        self.spc = spc

        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)

        # ---- graph ----
        self.spc.canvas.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        layout.addWidget(self.spc.canvas, 1)

        # ---- labels ----
        row = QHBoxLayout()
        row.addStretch()

        self.value_lbl = QLabel("--")
        self.status_lbl = QLabel("OK")

        self.value_lbl.setAlignment(Qt.AlignRight)
        self.status_lbl.setAlignment(Qt.AlignLeft)

        self.value_lbl.setStyleSheet("color:white; font-size:16pt;")
        self.status_lbl.setStyleSheet("color:lightgreen; font-size:16pt;")

        row.addWidget(self.value_lbl)
        row.addSpacing(10)
        row.addWidget(self.status_lbl)
        row.addStretch()

        layout.addLayout(row)

    def update_value(self, value):
        self.spc.update_graph(value)
        self.value_lbl.setText(f"{value:.2f}")

        zone = self.spc._scale_value(value)

        if zone <= 1 or zone >= 5:
            self.status_lbl.setText("Not_OK")
            self.status_lbl.setStyleSheet("color:red; font-size:16pt;")
        elif zone in (2, 4):
            self.status_lbl.setText("REWARK")
            self.status_lbl.setStyleSheet("color:yellow; font-size:16pt;")
        else:
            self.status_lbl.setText("OK")
            self.status_lbl.setStyleSheet("color:green; font-size:16pt;")
            
class SPCManager:
    def __init__(self, ui):
        self.ui = ui

        self.spcs = {
            1: SPCWidget(SPC_D1()),
            2: SPCWidget(SPC_D2()),
            3: SPCWidget(SPC_D3()),
            4: SPCWidget(SPC_D4()),
        }

        self.layouts = [
            ui.verticalLayout_2,
            ui.verticalLayout_3,
            ui.verticalLayout_4,
            ui.verticalLayout_5,
        ]

        self.containers = [
            ui.verticalLayout_2_container,
            ui.verticalLayout_3_container,
            ui.verticalLayout_4_container,
            ui.verticalLayout_5_container,
        ]

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

    def set_active_channels(self, channels):
        # clear everything
        for layout in self.layouts:
            self.clear_layout(layout)

        for c in self.containers:
            c.hide()

        for i, ch in enumerate(channels):
            self.layouts[i].addWidget(self.spcs[ch])
            self.containers[i].show()

    def update_value(self, channel, value):
        if channel in self.spcs:
            self.spcs[channel].update_value(value)
            
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.manager = SPCManager(self.ui)
        self.manager.set_active_channels([1, 2, 3, 4])

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.send_data)
        self.timer.start(1000)

    def send_data(self):
        values = [10, 20, 4, 56, 89, 78, 34, 60]
        for ch in [1, 2, 3, 4]:
            self.manager.update_value(ch, np.random.choice(values))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())