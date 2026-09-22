import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

class HistogramPlotter:
    def __init__(self, lower_limit=None, upper_limit=None):
        """
        Constructor: Initialize the matplotlib figure and axis for plotting.
        :param lower_limit: Lower limit for the x-axis.
        :param upper_limit: Upper limit for the x-axis.
        """
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        print("HistogramPlotter object created.")

    def __del__(self):
        """
        Destructor: Close the matplotlib figure to free resources.
        """
        plt.close(self.fig)
        print("HistogramPlotter object destroyed.")

    def plot_horizontal_histogram_with_bell_curve(self, data):
        """
        Plot a horizontal histogram with a bell curve overlay.
        :param data: List or array of data points.
        """
        # Clear the axis for new plot
        self.ax.clear()

        # Plot horizontal histogram with range to ensure bins within limits
        if self.lower_limit is not None and self.upper_limit is not None:
            n, bins, patches = self.ax.hist(data, bins=30, range=(self.lower_limit, self.upper_limit), orientation='horizontal', alpha=0.7, color='skyblue', edgecolor='black', label='Histogram')
        else:
            n, bins, patches = self.ax.hist(data, bins=30, orientation='horizontal', alpha=0.7, color='skyblue', edgecolor='black', label='Histogram')

        # Set y-ticks to bin edges for value labels at bin lines
        self.ax.set_yticks(bins)
        self.ax.set_yticklabels([f'{b:.3f}' for b in bins])

        # Fit a normal distribution to the data
        mu, std = np.mean(data), np.std(data)
        if self.lower_limit is not None and self.upper_limit is not None:
            y_vals = np.linspace(self.lower_limit, self.upper_limit, 100)
        else:
            y_vals = np.linspace(min(data), max(data), 100)
        p = norm.pdf(y_vals, mu, std)
        # Scale the PDF to match the histogram scale
        bin_width = (bins[-1] - bins[0]) / 30
        scale_factor = len(data) * bin_width
        self.ax.plot(p * scale_factor, y_vals, 'r-', linewidth=2, label='Bell Curve (Normal Fit)')

        # Set y-axis limits if provided (for horizontal histogram, values are on y-axis)
        if self.lower_limit is not None and self.upper_limit is not None:
            self.ax.set_ylim(self.lower_limit, self.upper_limit)

        # Set labels and title
        self.ax.set_xlabel('Frequency')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Horizontal Histogram with Bell Curve Overlay')
        self.ax.legend()
        self.ax.grid(True, alpha=0.3)

        # Display the plot
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == '__main__':
    # Create an object of the class with lower and upper limits
    plotter = HistogramPlotter(lower_limit=20.589, upper_limit=20.605)

    # Generate sample data (normally distributed for bell curve effect, clipped to limits)
    np.random.seed(42)  # For reproducibility
    sample_data = np.clip(np.random.normal(loc=20.597, scale=0.005, size=1000), 20.589, 20.605)

    # Check if any data is outside the limits
    print(f"Min data value: {min(sample_data):.6f}")
    print(f"Max data value: {max(sample_data):.6f}")
    print(f"Data outside limits: {any(d < 20.589 or d > 20.605 for d in sample_data)}")

    # Call the plotting method
    plotter.plot_horizontal_histogram_with_bell_curve(sample_data)
