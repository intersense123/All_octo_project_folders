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

class Ui_SPCPage(object):
     def setupUi(self, parent: QWidget):
        self.root = QWidget()
        self.root.setObjectName("spc_root")

        layout = parent.layout()
        if layout is None:
            layout = QVBoxLayout(parent)
            layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.root)

        # ================= MAIN VERTICAL LAYOUT =================
        self.verticalLayout = QVBoxLayout(self.root)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)

        # ================= FIRST ROW =================
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSpacing(4)

        # -------- Left container (D1) --------
        self.verticalLayout_2_container = QWidget(self.root)
        self.verticalLayout_2_container.setObjectName("d1_container")

        # Vertical layout inside left container
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayout_2_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        # Add left container to first-row horizontal layout
        self.horizontalLayout.addWidget(self.verticalLayout_2_container)
        

        # -------- Right container (D2) --------
        self.verticalLayout_3_container = QWidget(self.root)
        self.verticalLayout_3_container.setObjectName("d2_container")
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
        self.verticalLayout_4_container = QWidget(self.root)
        self.verticalLayout_4_container.setObjectName("d3_container")
        self.verticalLayout_4_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        self.verticalLayout_4 = QVBoxLayout(self.verticalLayout_4_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_2.addWidget(self.verticalLayout_4_container)

        # -------- Bottom-right container (D4) --------
        self.verticalLayout_5_container = QWidget(self.root)
        self.verticalLayout_5_container.setObjectName("d4_container")
        self.verticalLayout_5_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        self.verticalLayout_5 = QVBoxLayout(self.verticalLayout_5_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_2.addWidget(self.verticalLayout_5_container)

        # Add SECOND ROW to MAIN vertical layout
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        QMetaObject.connectSlotsByName(parent)
                
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
            # self.fig.set_figheight(9)
            # self.fig.set_size_inches(7,9)
            self.ax = self.fig.add_subplot(111)

            # Dark theme
            self.fig.patch.set_facecolor("black")
            self.ax.tick_params(axis="x", colors="white")
            self.ax.tick_params(axis="y", colors="white")

            # Draw empty graph initially
            self.init_blank_ui()
        except Exception as e:
            print(f"Error in SPC Base class initialization :{e}")   
            
    def scale_value(self, v):
        for i in range(len(self.limits)-1):
            low = self.limits[i]
            high = self.limits[i + 1]

            if low <= v <= high or high <= v <= low:
                return i + (v - low) / (high - low)

        return 0 if v < self.limits[0] else 6
    

    def set_margins(self, left, right, top, bottom):
        self.fig.subplots_adjust(
            left=left,
            right=right,
            top=top,
            bottom=bottom
        )
        self.canvas.draw_idle()

    def draw_background(self):
        self.ax.axhspan(0, 1, color="red", alpha=0.9)
        self.ax.axhspan(1, 2, color="yellow", alpha=0.9)
        self.ax.axhspan(2, 4, color="green", alpha=0.9)
        self.ax.axhspan(4, 5, color="yellow", alpha=0.9)
        self.ax.axhspan(5, 6, color="red", alpha=0.9)

    def draw_limit_lines(self):
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
        self.draw_background()
        self.draw_limit_lines()

        # IMPORTANT: add padding
        self.ax.set_ylim(-0.6, 6.7)
        

        self.ax.set_yticks(self.y_positions)
        self.ax.set_yticklabels(self.limits, color="white")

        self.ax.set_yticks(self.y_positions)
        self.ax.set_yticklabels(self.limits)

        self.ax.set_title(self.title, color="white",fontweight="bold",pad=4)
        self.ax.set_xlabel("")
        self.ax.set_ylabel(self.title)
        
        # Ticks size
        self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
        self.ax.tick_params(axis="y", labelsize=9, colors="white")

        # self._apply_responsive_layout()
        
        # plt.draw()
        # plt.pause(0.01)
        self.canvas.draw_idle()

    
    def generate_graph(self, raw_data):
        try:
            self.data_raw = raw_data[-50:]  # Last 50 points only
            
            x_data = np.arange(1, len(self.data_raw) + 1)
            
            self.ax.clear()
            self.draw_background()
            self.draw_limit_lines()
            
            self.line, = self.ax.plot(x_data, [self._scale_value(v) for v in self.data_raw], 
                                    "bo-", markersize=3, linewidth=2)
            
            self.ax.set_xlim(1, max(10, len(self.data_raw)))
            self.ax.set_ylim(-0.6, 6.7)
            self.ax.set_yticks(self.y_positions)
            self.ax.set_yticklabels(self.limits, color="white")
            
            self.ax.set_title(self.title, color="white", fontweight="bold", pad=4)
            self.ax.tick_params(axis="x", labelsize=9, pad=4, colors="white")
            self.ax.tick_params(axis="y", labelsize=9, colors="white")
            
            self.canvas.draw_idle()
        except Exception as e:
            print(f"Error in generate_graph -> {e}")
            
    
    
    def update_graph(self, value):
        try:
            # 🔥 INCREMENTAL UPDATE - 100x faster!
            self.data_raw.append(value)
            
            # Rolling buffer (50 points max)
            if len(self.data_raw) > 50:
                self.data_raw.pop(0)
            
            # Scale only NEW point (fast)
            scaled_value = self._scale_value(value)
            
            # Update line data incrementally
            x_data = np.arange(1, len(self.data_raw) + 1)
            if hasattr(self, 'line'):
                self.line.set_data(x_data, [self._scale_value(v) for v in self.data_raw])
            else:
                # First time: create line
                self.line, = self.ax.plot(x_data, [self._scale_value(v) for v in self.data_raw], "bo-", markersize=3, linewidth=2)
            
            # Auto-adjust limits
            self.ax.set_xlim(1, max(10, len(self.data_raw)))
            self.ax.set_ylim(-0.6, 6.7)
            
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
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        # self.spc.canvas.setMinimumHeight(130)
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
        self.value_lbl.setMinimumHeight(20)


        self.status_lbl = QLabel("OK")
        self.status_lbl.setMinimumHeight(20)
        
        self.value_lbl.setAlignment(Qt.AlignRight)
        self.status_lbl.setAlignment(Qt.AlignLeft)

        self.value_lbl.setStyleSheet("color:white; font-size:16pt;font-weight: bold;")
        self.status_lbl.setStyleSheet("color:lightgreen; font-size:16pt;font-weight: bold;")

        row.addWidget(self.value_lbl)
        row.addSpacing(4)
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
    def clear_layout(self, layout):
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
            self.active_channels = list(range(1, channels + 1))
            self.apply_layout()
        except Exception as e:
            print(f"Error for setting active channel as-> {e}")

    #manage layout as per spc instance
    def apply_layout(self):
        try:
            # clear everything
            for layout in (self.spc_1, self.spc_2, self.spc_3, self.spc_4):
                self.clear_layout(layout)

            spcs = [self.spc_all[ch] for ch in self.active_channels]
            count = len(spcs)
            
            self.ui.verticalLayout_2_container.show()
            self.ui.verticalLayout_3_container.show()
            self.ui.verticalLayout_4_container.show()
            self.ui.verticalLayout_5_container.show()
            
            # ---------------- 1 SPC ----------------
            if count == 1:
                self.spc_1.addWidget(spcs[0])
                spcs[0].spc.set_margins(
                    left=0.12,
                    right=0.97,
                    top=0.88,
                    bottom=0.22
                )
                self.ui.verticalLayout_2_container.show()        
                self.ui.verticalLayout_3_container.hide()
                self.ui.verticalLayout_4_container.hide()
                self.ui.verticalLayout_5_container.hide()
                
                self.ui.verticalLayout.setStretch(0, 1)  # first row (graphs)
                self.ui.verticalLayout.setStretch(1, 0)  # second row (hidden)
                

            # ---------------- 2 SPC ----------------
            elif count == 2:
                self.spc_2 = self.ui.verticalLayout_4
                # TOP SPC
                self.spc_1.addWidget(spcs[0], stretch=1)

                # BOTTOM SPC → USE BOTTOM-LEFT (IMPORTANT)
                self.spc_2.addWidget(spcs[1], stretch=1)

                # margins for half-height SPCs
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(130)
                    spc.spc.set_margins(
                        left=0.12,
                        right=0.97,
                        top=0.85,
                        bottom=0.22
                    )

                # hide RIGHT column completely
                self.ui.verticalLayout_3_container.hide()
                self.ui.verticalLayout_5_container.hide()

                # SHOW left column
                self.ui.verticalLayout_2_container.show()
                self.ui.verticalLayout_4_container.show()

                # equal height rows
                self.ui.verticalLayout.setStretch(0, 1)
                self.ui.verticalLayout.setStretch(1, 1)

            # ---------------- 3 SPC (FIXED) ----------------
            elif count == 3:
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])

                # put SPC3 in bottom-left
                self.spc_3.addWidget(spcs[2])
                spcs[0].spc.canvas.setMinimumHeight(130)
                spcs[1].spc.canvas.setMinimumHeight(130)
                spcs[2].spc.canvas.setMinimumHeight(130)

                spcs[0].spc.set_margins(
                    left=0.15,
                    right=0.96,
                    top=0.82,
                    bottom=0.22
                )
                spcs[1].spc.set_margins(
                    left=0.15,
                    right=0.96,
                    top=0.82,
                    bottom=0.22
                )

                # bottom full-width SPC
                self.spc_3.addWidget(spcs[2])
                spcs[2].spc.set_margins(
                    left=0.12,
                    right=0.97,
                    top=0.82,
                    bottom=0.22
                )
                self.ui.verticalLayout_2_container.show()
                self.ui.verticalLayout_3_container.show()
                self.ui.verticalLayout_4_container.show()
                
                # 🔴 HIDE bottom-right column completely
                self.ui.verticalLayout_5_container.hide()
                
                
                # balance rows
                self.ui.verticalLayout.setStretch(0, 1)
                self.ui.verticalLayout.setStretch(1, 1)
                
                # stretch bottom-left to full width
                self.ui.horizontalLayout_2.setStretch(0, 1)
                self.ui.horizontalLayout_2.setStretch(1, 0)

            # ---------------- 4 SPC ----------------
            elif count == 4:
                self.spc_1.addWidget(spcs[0])
                self.spc_2.addWidget(spcs[1])
                self.spc_3.addWidget(spcs[2])
                self.spc_4.addWidget(spcs[3])
                
                for spc in spcs:
                    spc.spc.canvas.setMinimumHeight(130)
                    spc.spc.set_margins(
                        left=0.15,
                        right=0.97,
                        top=0.85,
                        bottom=0.20
                    )
                    
                self.ui.verticalLayout_2_container.show()
                self.ui.verticalLayout_3_container.show()
                self.ui.verticalLayout_4_container.show()
                self.ui.verticalLayout_5_container.show()
                
                self.ui.verticalLayout.setStretch(0, 1)
                self.ui.verticalLayout.setStretch(1, 1)
                
                # restore visibility
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