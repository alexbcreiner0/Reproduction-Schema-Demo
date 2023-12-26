import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_pgf import FigureCanvasPgf

class LatexViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Latex Viewer")

        self.setup_gui()

    def setup_gui(self):
        # Entry widget for entering LaTeX code
        self.latex_entry = ttk.Entry(self.root, width=40)
        self.latex_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to render LaTeX code
        render_button = ttk.Button(self.root, text="Render", command=self.render_latex)
        render_button.grid(row=0, column=1, padx=10, pady=10)

        # Label to display rendered LaTeX image
        self.latex_label = ttk.Label(self.root)
        self.latex_label.grid(row=1, column=0, columnspan=2, pady=10)

    def render_latex(self):
        # Get LaTeX code from the entry widget
        latex_code = self.latex_entry.get()

        # Create a Matplotlib figure and render LaTeX code
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"${latex_code}$", fontsize=16, ha='center', va='center')

        # Convert the Matplotlib figure to a Tkinter PhotoImage
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        photo_img = tk.PhotoImage(master=self.root)
        photo_img.tk.call(canvas._tkcanvas, 'get', 'image', photo_img, 'all')
        
        # Update the label with the rendered LaTeX image
        self.latex_label.configure(image=photo_img)
        self.latex_label.image = photo_img

if __name__ == "__main__":
    root = tk.Tk()
    app = LatexViewerApp(root)
    root.mainloop()
