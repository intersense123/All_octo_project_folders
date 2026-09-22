import matplotlib.pyplot as plt
import numpy as np

class SPCPlot:
    def __init__(self, lol, lsl, lcl, nominal, ucl, usl, uol):
        self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
        self.lol = lol
        self.uol = uol

        self.data_raw = []
        self.data_scaled = []

        # fixed Y positions: 0..6
        self.y_positions = np.arange(7)

    def add_data(self, values):
        """Store raw values and create clipped versions for plotting."""
        self.data_raw.extend(values)

        # Scale without modifying original data
        clipped = []
        for v in values:
            if v < self.lol:
                clipped.append(self.lol)
            elif v > self.uol:
                clipped.append(self.uol)
            else:
                clipped.append(v)

        self.data_scaled.extend(clipped)

    def plot(self):
        x = np.arange(len(self.data_scaled))

        plt.figure(figsize=(10, 5))
        plt.plot(x, self.data_scaled, marker='o', linestyle='-', label="Scaled Data")

        # Draw specification lines
        labels = ["LOL", "LSL", "LCL", "Nominal", "UCL", "USL", "UOL"]
        for y, label in zip(self.limits, labels):
            plt.axhline(y, linestyle='--', linewidth=1, alpha=0.7, label=label)

        plt.legend()
        plt.grid(True)
        plt.title("SPC Plot with Clipped Values")
        plt.show()
