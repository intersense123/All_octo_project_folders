import matplotlib.pyplot as plt
import numpy as np

class SPCPlot:
    def __init__(self, lol, lsl, lcl, nominal, ucl, usl, uol):
        self.limits = [lol, lsl, lcl, nominal, ucl, usl, uol]
        self.data_scaled = []
        self.data_raw = []

        # fixed Y positions: 0..6
        self.y_positions = np.arange(7)

        # colors for lines (red, red, yellow, green, yellow, red, red)
        self.line_colors = ["red", "red", "yellow", "green", "yellow", "red", "red"]
        self.line_styles = ["-", "--", ":", "-.", ":", "--", "-"]

        self.fig, self.ax = plt.subplots(figsize=(5, 2))

        self.fig.patch.set_facecolor("black")
        # self.ax.set_facecolor("black")

        self.ax.xaxis.label.set_color("white")
        self.ax.yaxis.label.set_color("white")

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')

    # ---------------------------------------------------
    # 1. INIT BLANK UI
    # ---------------------------------------------------
    def init_blank_ui(self):
        self.ax.clear()
        self._draw_background()
        self._draw_limit_lines()

        self.ax.set_xlabel("Job Counts")
        self.ax.set_ylabel("Dimension D1")

        # set Y ticks to original SPC values
        self.ax.set_yticks(self.y_positions)
        self.ax.set_yticklabels([str(v) for v in self.limits])

        self.ax.set_ylim(-0.5, 6.5)
        plt.draw()
        plt.pause(0.01)

    # ---------------------------------------------------
    # Normalization function
    # ---------------------------------------------------
    def _scale_value(self, v):
        """
        Convert actual value v → normalized Y scale (0 to 6)
        by finding which two SPC lines it lies between.
        """
        for i in range(6):
            low = self.limits[i]
            high = self.limits[i+1]

            if low <= v <= high or high <= v <= low:
                # ratio between two lines
                ratio = (v - low) / (high - low)
                return i + ratio

        # Below lol
        if v < self.limits[0]:
            return 0

        # Above uol
        if v > self.limits[-1]:
            return 6

        return None

    # ---------------------------------------------------
    # Draw background colored zones
    # ---------------------------------------------------
    def _draw_background(self):
        # red bottom: lol → lsl (0→1)
        self.ax.axhspan(0, 1, color="red", alpha=0.8)#0.25)
        # yellow: lsl → lcl (1→2)
        self.ax.axhspan(1, 2, color="yellow", alpha=0.8)#0.25)
        # green: lcl → ucl (2→4)
        self.ax.axhspan(2, 4, color="green", alpha=0.8)#0.25)
        # yellow: ucl → usl (4→5)
        self.ax.axhspan(4, 5, color="yellow", alpha=0.8)#0.25)
        # red top: usl → uol (5→6)
        self.ax.axhspan(5, 6, color="red", alpha=0.8)#0.25)

    # ---------------------------------------------------
    # Draw 7 SPC limit lines
    # ---------------------------------------------------
    def _draw_limit_lines(self):

        xmin = 0
        xmax = len(self.data_raw)

        for i in range(7):
            self.ax.hlines(
                self.y_positions[i],
                xmin=xmin,
                xmax=xmax,
                colors=self.line_colors[i],
                linestyles=self.line_styles[i],
                linewidth=1.5
            )

    # ---------------------------------------------------
    # 2. GENERATE FULL GRAPH FROM LIST
    # ---------------------------------------------------
    def generate_graph(self, raw_data):
        self.data_raw = raw_data
        self.data_scaled = [self._scale_value(v) for v in raw_data]

        self.ax.clear()
        self._draw_background()
        self._draw_limit_lines()

        # plot blue line & dots
        # x = np.arange(len(self.data_scaled))
        x = np.arange(1, len(self.data_scaled) + 1)
        self.ax.plot(x, self.data_scaled, marker="o", color="blue", linestyle="-", markersize=3)

        # fix axis
        self.ax.set_ylim(-0.5, 6.5)

        # static labels
        self.ax.set_yticks(self.y_positions)
        self.ax.set_yticklabels([str(v) for v in self.limits])
        self.ax.set_xlabel("Job Counts")
        self.ax.set_ylabel("Dimension D1")
        # self.ax.set_xticklabels([str(i) for i in x])
        self.ax.yaxis.label.set_color("white")

        plt.draw()
        plt.pause(0.01)

    # ---------------------------------------------------
    # 3. UPDATE GRAPH WITH ONE NEW VALUE
    # ---------------------------------------------------
    def update_graph(self, new_value):
        self.data_raw.append(new_value)
        self.data_raw.pop(0)  # remove oldest value
        self.data_scaled.append(self._scale_value(new_value))
        self.data_scaled.pop(0)  # remove oldest scaled value

        self.generate_graph(self.data_raw)

    def __del__(self):
        """Destructor: safely close the Matplotlib figure to free memory."""
        try:
            plt.close(self.fig)
        except Exception:
            pass

# ---------------------------------------------------
# Example usage
# ---------------------------------------------------
if __name__ == "__main__":
    spc = SPCPlot(
        lol=10,
        lsl=25, 
        lcl=50, 
        nominal=55, 
        ucl=60, 
        usl=70, 
        uol=150
    )

    spc.init_blank_ui()
    spc.generate_graph([
    143, 57, 22, 118, 76, 149, 35, 14, 129, 88,
    46, 137, 53, 109, 72, 144, 18, 101, 67, 150,
    144, 18, 101, 67, 150
    ])
    spc.update_graph(52)
    spc.update_graph(52)
    spc.update_graph(52)
    spc.update_graph(52)
    spc.update_graph(52)
    plt.show()
    # del spc
    # spc.__del__()
