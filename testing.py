import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib import rcParams

def get_text(file_name):
	with open(file_name, 'r') as file:
		text = r'' + file.read()
		return text

window = tk.Tk()
text = get_text('exploitation.txt')
fig, ax = plt.subplots()

ax.axis("off")
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

ax.text(x = 0, y = 1, s = f"{text}", ha = 'left', va = 'top', size=10, wrap = True)

canvas = tk.Canvas(window, bg = 'white', width = 1920)
rendered_latex = FigureCanvasTkAgg(fig, master = canvas)
rendered_latex.draw()
rendered_latex.get_tk_widget().pack(fill = 'both')

y_scrollbar = tk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
x_scrollbar = tk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)

y_scrollbar.pack(side = 'right', fill = 'y')
x_scrollbar.pack(side = 'bottom', fill = 'x')

canvas.config(yscrollcommand = y_scrollbar.set, scrollregion = (0,0,3000,5000), xscrollcommand = x_scrollbar.set)
canvas.pack(fill = 'both')



window.mainloop()
