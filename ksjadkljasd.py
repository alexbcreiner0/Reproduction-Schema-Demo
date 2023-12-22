import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class LatexRendererApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Environment LaTeX Renderer")

        self.setup_ui()

    def setup_ui(self):
        # Create a Text widget for entering LaTeX code
        self.latex_entry = tk.Text(self.root, wrap=tk.WORD, height=5, width=40)
        self.latex_entry.insert(tk.END, r'\parbox{0.8\linewidth}{This is a paragraph with math environments: $E=mc^2$, $F=ma$, and $a^2+b^2=c^2$.}')
        self.latex_entry.pack(pady=10)

        # Create a button to render LaTeX code
        render_button = tk.Button(self.root, text="Render LaTeX", command=self.render_latex)
        render_button.pack(pady=5)

        # Create a canvas to display the rendered LaTeX
        self.canvas = tk.Canvas(self.root, width=400, height=200, bg="white")
        self.canvas.pack(pady=10)

    def render_latex(self):
        # Get LaTeX code from the entry widget
        latex_code = self.latex_entry.get("1.0", tk.END).strip()

        # Clear the canvas
        self.canvas.delete("all")

        # Render LaTeX using matplotlib
        fig, ax = plt.subplots(figsize=(4, 2))
        ax.text(0.5, 0.5, f"${latex_code}$", size=14, ha='center', va='center', multialignment='center')
        ax.axis('off')

        # Display the rendered LaTeX on the canvas
        self.rendered_latex = FigureCanvasTkAgg(fig, master=self.canvas)
        self.rendered_latex.draw()
        self.rendered_latex.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.rendered_latex.get_tk_widget().bind("<Configure>", self.resize_canvas)

    def resize_canvas(self, event):
        # Resize the canvas when the window size changes
        self.rendered_latex.get_tk_widget().configure(scrollregion=self.rendered_latex.get_tk_widget().bbox("all"))

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    root = tk.Tk()
    app = LatexRendererApp(root)
    root.mainloop()
