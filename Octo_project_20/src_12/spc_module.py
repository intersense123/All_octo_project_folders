from PySide2.QtWidgets import (
    QMainWindow, QWidget, QGridLayout,QApplication
)
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QLabel
import random
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys

class SPCBase:
    def __init__(self, label: QLabel, title="D1"):
        """
        label  → QLabel to display current value
        title  → Dimension name (D1, D2...)
        """

        self.label = label
        self.title = title

        self.data_raw = []
        self.data_scaled = []

        # SPC limits (example – change per dimension)
        self.limits = [0, 10, 20, 30, 40, 50, 60]
        self.y_positions = np.arange(7)

        # ---- matplotlib ----
        self.fig = Figure(figsize=(5, 2))
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)

        self._init_ui()
    
    def _init_ui(self):
        self.ax.clear()
        self._draw_background()
        self._draw_limits()

        self.ax.set_ylabel(self.title)
        self.ax.set_ylim(-0.5, 6.5)
        self.canvas.draw_idle()
        
    def _scale_value(self, v: float):
        for i in range(6):
            low = self.limits[i]
            high = self.limits[i + 1]

            if low <= v <= high or high <= v <= low:
                return i + (v - low) / (high - low)

        if v < self.limits[0]:
            return 0
        if v > self.limits[-1]:
            return 6
        
    def _draw_background(self):
        self.ax.axhspan(0, 1, color="red", alpha=0.3)
        self.ax.axhspan(1, 2, color="yellow", alpha=0.3)
        self.ax.axhspan(2, 4, color="green", alpha=0.3)
        self.ax.axhspan(4, 5, color="yellow", alpha=0.3)
        self.ax.axhspan(5, 6, color="red", alpha=0.3)

    def _draw_limits(self):
        for y in self.y_positions:
            self.ax.hlines(y, 0, len(self.data_raw), colors="white", linewidth=1)
            
    def update_value(self, value: float):
        """
        Update label and SPC graph
        """

        # 1️⃣ Update QLabel
        self.label.setText(f"{value:.3f}")

        # Optional: color logic
        if value < self.limits[1] or value > self.limits[5]:
            self.label.setStyleSheet("color:red;")
        else:
            self.label.setStyleSheet("color:lime;")

        # 2️⃣ Update SPC graph
        self.data_raw.append(value)
        if len(self.data_raw) > 20:
            self.data_raw.pop(0)

        scaled = [self._scale_value(v) for v in self.data_raw]

        self.ax.clear()
        self._draw_background()
        self._draw_limits()

        x = np.arange(1, len(scaled) + 1)
        self.ax.plot(x, scaled, marker="o", color="cyan")
        self.ax.set_ylabel(self.title)
        self.ax.set_ylim(-0.5, 6.5)

        self.canvas.draw_idle()
    
    




