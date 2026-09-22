from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel,QSizePolicy,
    QVBoxLayout, QWidget)
from PySide2.QtCore import QTimer
import sys
import numpy as np
import matplotlib.pyplot as plt
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
        self.verticalLayout_2_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        # Add left container to first-row horizontal layout
        self.horizontalLayout.addWidget(self.verticalLayout_2_container)
        

        # -------- Right container (D2) --------
        self.verticalLayout_3_container = QWidget(self.widget)
        self.verticalLayout_3_container.setObjectName("verticalLayout_3_container")
        self.verticalLayout_3_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )


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
        self.verticalLayout_4_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        self.verticalLayout_4 = QVBoxLayout(self.verticalLayout_4_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_2.addWidget(self.verticalLayout_4_container)

        # -------- Bottom-right container (D4) --------
        self.verticalLayout_5_container = QWidget(self.widget)
        self.verticalLayout_5_container.setObjectName("verticalLayout_5_container")
        self.verticalLayout_5_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

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

    def __init__(self, title, lol, lsl, lcl, nominal, ucl, usl, uol):
        try:
            self.title = title                  # Graph title (D1, D2, ...)
            self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]                # SPC limits

            self.data_raw = []                  # Raw input values
            self.data_scaled = []               # Scaled values for plotting

            self.y_positions = np.arange(7)     # 7 SPC zones

            # Colors and styles for limit lines
            self.line_colors = ["red","red","yellow","green","yellow","red","red"]
            self.line_styles = ["-","--",":","-.",":","--","-"]

            # Create matplotlib figure and canvas
            self.fig = Figure()#Figure(figsize=(4.5, 2.2))
            self.canvas = FigureCanvas(self.fig)
            self.fig.set_size_inches(6,3)
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
        for i in range(len(self.limits)-1):
            low = self.limits[i]
            high = self.limits[i + 1]

            if low <= v <= high or high <= v <= low:
                return i + (v - low) / (high - low)

        return 0 if v < self.limits[0] else 6
    
    def _apply_responsive_layout(self):
        """
        Adjust margins dynamically for 800x480 and similar screens
        """
        try:
            self.fig.tight_layout(pad=0.3)

            # fallback margins (safe for embedded)
            self.fig.subplots_adjust(
                left=0.18,     # space for Y labels
                right=0.97,
                top=0.88,
                bottom=0.20    # space for X ticks
            )
        except Exception:
            pass


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
                    linewidth=1.5
                )
        except Exception as e:
            print("Error in draw_limit_lines -> {e}")
    
    def init_blank_ui(self):
        self.ax.clear()
        self._draw_background()
        self._draw_limit_lines()

        # IMPORTANT: add padding
        self.ax.set_ylim(-0.6, 6.8)
        

        self.ax.set_yticks(self.y_positions)
        self.ax.set_yticklabels(self.limits, color="white")

        self.ax.set_yticks(self.y_positions)
        self.ax.set_yticklabels(self.limits)

        self.ax.set_title(self.title, color="white",fontweight="bold")
        self.ax.set_xlabel("")
        self.ax.set_ylabel(self.title)
        
        # Ticks size
        self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
        self.ax.tick_params(axis="y", labelsize=9, colors="white")

        self._apply_responsive_layout()
        
        # plt.draw()
        # plt.pause(0.01)
        self.canvas.draw_idle()

    
    def generate_graph(self, raw_data):
        try:
            self.data_raw = raw_data
            self.data_scaled = [self._scale_value(v) for v in raw_data]

            self.ax.clear()
            self._draw_background()
            self._draw_limit_lines()

            x = np.arange(1, len(self.data_scaled) + 1)
            self.ax.plot(x, self.data_scaled, "bo-", markersize=3)
            
            # IMPORTANT: add padding
            self.ax.set_ylim(-0.6, 6.8)
            

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits, color="white")

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white",fontweight="bold")
            self.ax.set_xlabel("")
            self.ax.set_ylabel(self.title)

            # Ticks size
            self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
            self.ax.tick_params(axis="y", labelsize=9, colors="white")

            self._apply_responsive_layout()
        
            # plt.draw()
            # plt.pause(0.01)
        except Exception as e:
            print("Erro in gnerate_graph -> {e}")
            
    
    
    def update_graph(self, value):
        try:
            self.data_raw.append(value)

            if len(self.data_raw) > 30:
                self.data_raw.pop(0)

            scaled = [self._scale_value(v) for v in self.data_raw]

            self.ax.clear()
            self._draw_background()
            self._draw_limit_lines()

            x = np.arange(1, len(scaled) + 1)
            self.ax.plot(x, scaled, "bo-", markersize=3)
            
            # IMPORTANT: add padding
            self.ax.set_ylim(-0.6,6.8)
            

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits, color="white")

            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits)

            self.ax.set_title(self.title, color="white",fontweight="bold")
            self.ax.set_xlabel("")
            self.ax.set_ylabel(self.title)

            # Ticks size
            self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
            self.ax.tick_params(axis="y", labelsize=9, colors="white")

            self._apply_responsive_layout()
            
            self.generate_graph(self.data_raw)
            self.canvas.draw_idle()
        except Exception as e:
            print(f"Error in update_graph -> {e}")
            
    def __del__(self):
        """Destructor: safely close the Matplotlib figure to free memory."""
        try:
            self.canvas.close(self.fig)
        except Exception:
            pass   
        
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
        self.value_lbl.setMinimumHeight(30)


        self.status_lbl = QLabel("OK")
        self.status_lbl.setMinimumHeight(30)
        
        self.value_lbl.setAlignment(Qt.AlignRight)
        self.status_lbl.setAlignment(Qt.AlignLeft)

        self.value_lbl.setStyleSheet("color:white; font-size:16pt;font-weight: bold;")
        self.status_lbl.setStyleSheet("color:lightgreen; font-size:16pt;font-weight: bold;")

        row.addWidget(self.value_lbl)
        row.addSpacing(5)
        row.addWidget(self.status_lbl)
        row.addStretch()

        layout.addLayout(row)

    def update_value(self, value):
        self.spc.update_graph(value)
        self.value_lbl.setText(f"{value:.3f}")

        zone = self.spc._scale_value(value)

        if zone <= 1 or zone >= 6:
            self.status_lbl.setText("Not OK")
            self.status_lbl.setStyleSheet("color:red; font-size:16pt;font-weight: bold;")
        elif zone in (2, 4):
            self.status_lbl.setText("Rework")
            self.status_lbl.setStyleSheet("color:yellow; font-size:16pt;font-weight: bold;")
        else:
            self.status_lbl.setText("OK")
            self.status_lbl.setStyleSheet("color:green; font-size:16pt;font-weight: bold;")
                
class SPCManager:
    def __init__(self, ui):
        try:
            self.ui = ui
            
            self.spc_all = {
            1: SPCWidget(SPCBase("D1", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            2: SPCWidget(SPCBase("D2", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            3: SPCWidget(SPCBase("D3", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            4: SPCWidget(SPCBase("D4", lol=20.000,lsl=20.010,lcl=20.015,nominal=20.020,ucl=20.025,usl=20.030,uol=20.042)),
            }


            self.active_channels = []

            # Layouts from Qt Designer
            self.spc_1 = ui.verticalLayout_2
            self.spc_2 = ui.verticalLayout_3
            self.spc_3 = ui.verticalLayout_4
            self.spc_4 = ui.verticalLayout_5

            ui.horizontalLayout.setStretch(0, 1)
            ui.horizontalLayout.setStretch(1, 1)
            ui.horizontalLayout_2.setStretch(0, 1)
            ui.horizontalLayout_2.setStretch(1, 1)

            # ✅ ROW stretch (THIS WAS MISSING)
            ui.verticalLayout.setStretch(0, 1)
            ui.verticalLayout.setStretch(1, 1)
            

        except Exception as e:
            print(f"Error in intialization of SPCManager :-> {e}")
                
    #clear layout for first time
    def _clear_layout(self, layout):
        try:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().setParent(None)
        except Exception as e:
            print(f"Error in clear_layout:-> {e}")

    #set active channels
    def set_active_channels(self, channels):
        try:
            self.active_channels = channels
            self._apply_layout()
        except Exception as e:
            print(f"Error for setting active channel as-> {e}")

    #manage layout as per spc instance
    def _apply_layout(self):
        try:
            # clear everything
            for layout in (self.spc_1, self.spc_2, self.spc_3, self.spc_4):
                self._clear_layout(layout)

            spcs = [self.spc_all[ch] for ch in self.active_channels]
            count = len(spcs)
            
            self.ui.verticalLayout_2_container.show()
            self.ui.verticalLayout_3_container.show()
            self.ui.verticalLayout_4_container.show()
            self.ui.verticalLayout_5_container.show()
        

            # ---------------- 1 SPC ----------------
            if count == 1:
                self.spc_1.addWidget(spcs[0])
                self.ui.verticalLayout_2_container.show()
                
                self.ui.verticalLayout_3_container.hide()
                self.ui.verticalLayout_4_container.hide()
                self.ui.verticalLayout_5_container.hide()
                
                self.ui.verticalLayout.setStretch(0, 1)  # first row (graphs)
                self.ui.verticalLayout.setStretch(1, 0)  # second row (hidden)
                

            # ---------------- 2 SPC ----------------
            elif count == 2:
                self.spc_2 = self.ui.verticalLayout_5
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])
                
                
                # self.ui.verticalLayout_4_container.hide()
               
                # show only needed containers
                self.ui.verticalLayout_2_container.show()
                self.ui.verticalLayout_4_container.hide()

                # hide unused column containers
                self.ui.verticalLayout_3_container.hide()
                self.ui.verticalLayout_5_container.show()

                # stretch rows equally
                self.ui.verticalLayout.setStretch(0, 1)
                self.ui.verticalLayout.setStretch(1, 1)
                self.ui.verticalLayout_2.setStretch(0, 1)
                self.ui.verticalLayout_2.setStretch(1, 1)

            # ---------------- 3 SPC (FIXED) ----------------
            elif count == 3:
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])

                # put SPC3 in bottom-left
                self.spc_3.addWidget(spcs[2])

                self.ui.verticalLayout_3_container.show()
                self.ui.verticalLayout_4_container.show()
                # 🔴 HIDE bottom-right column completely
                self.ui.verticalLayout_5_container.hide()
                
                # stretch bottom-left to full width
                self.ui.horizontalLayout_2.setStretch(0, 1)
                self.ui.horizontalLayout_2.setStretch(1, 0)

            # ---------------- 4 SPC ----------------
            elif count == 4:
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])
                self.spc_3.addWidget(spcs[2])
                self.spc_4.addWidget(spcs[3])

                # restore visibility
                self.ui.verticalLayout_5_container.show()
                self.ui.horizontalLayout_2.setStretch(0, 1)
                self.ui.horizontalLayout_2.setStretch(1, 1)
        except Exception as e:
            print(f"Error while applying layout -> {e}")
            
    #update value on spc chanrt as per active channels
    def update_value(self, channel, value):
        if channel in self.active_channels:
            self.spc_all[channel].update_value(value)

    
# class MainWindow(QMainWindow):
#     def __init__(self):
        
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         self.spc_manager = SPCManager(self.ui)

#         # ✅ CHANGE THIS ONLY
#         self.spc_manager.set_active_channels([1,2,3,4])
#             # try [1], [1,2], [1,2,3], [1,2,3,4]

#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.send_data)
#         self.timer.start(1000)
 
#     #pass data to spc chart one by one
#     def send_data(self):
#         try:
#             for ch in self.spc_manager.active_channels:
#                 for value in [20.007,20.019,20.022,20.026,20.027,20.033,20.041]:
#                     self.spc_manager.update_value(ch, value)
#         except Exception as e:
#             print(f"Error in sending data ->{e}")            

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())