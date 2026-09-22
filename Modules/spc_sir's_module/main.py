import sys
import numpy as np
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import spc
import spc_1

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = spc.Ui_MainWindow()
        self.ui.setupUi(self)

        # Fixed limits for SPCPlot
        lol, lsl, lcl, nominal, ucl, usl, uol = 10, 25, 50, 55, 60, 70, 150

        # List of widgets
        widgets = [self.ui.widget, self.ui.widget_2, self.ui.widget_3, self.ui.widget_4]

        for widget in widgets:
            # Create canvas
            canvas = FigureCanvas()

            # Create SPCPlot
            spc_plot = spc_1.SPCPlot(lol, lsl, lcl, nominal, ucl, usl, uol)

            # Generate 50 random values
            random_values = np.random.uniform(lol, uol, 50)

            # Generate graph
            spc_plot.generate_graph(random_values.tolist())

            # Embed canvas into widget
            layout = QtWidgets.QVBoxLayout(widget)
            layout.addWidget(canvas)
            canvas.figure = spc_plot.fig

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
