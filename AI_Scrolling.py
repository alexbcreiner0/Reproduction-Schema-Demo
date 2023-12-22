import matplotlib.pyplot as plt
import numpy as np
import mplcursors

class InteractiveGraph:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.func = lambda x: x**2  # Example quadratic function
        self.initialize_plot()
        mplcursors.cursor(hover=True).connect("add", self.on_cursor)

    def initialize_plot(self):
        x = np.linspace(-10, 10, 1000)
        y = self.func(x)
        self.line, = self.ax.plot(x, y, label="Function")
        self.ax.set_title("Interactive Graph")
        self.ax.legend()
        plt.show()

    def on_cursor(self, sel):
        x = sel.cursor[0]
        y = sel.cursor[1]
        self.update_plot(x, y)

    def update_plot(self, x, y):
        x_range = self.ax.get_xlim()
        y_range = self.ax.get_ylim()

        x_center = x_range[0] + (x_range[1] - x_range[0]) / 2
        y_center = y_range[0] + (y_range[1] - y_range[0]) / 2

        x_offset = x_center - x
        y_offset = y_center - y

        self.ax.set_xlim(x_range[0] - x_offset, x_range[1] - x_offset)
        self.ax.set_ylim(y_range[0] - y_offset, y_range[1] - y_offset)

        plt.draw()

if __name__ == "__main__":
    interactive_graph = InteractiveGraph()
    plt.show()
