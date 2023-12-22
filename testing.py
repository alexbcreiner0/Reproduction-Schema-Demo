import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib import rcParams

def get_text(file_name):
	with open(file_name, 'r') as file:
		text = r'' + file.read().strip()
		return text

text = get_text('exploitation.txt')
fig, ax = plt.subplots()
ax.set_xlim(0,5)
ax.set_ylim(0,5)
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
fuck = ax.text(x = 0, y = 5, s = text, size=10, ha = 'left', va = 'top', wrap = True)
fuck = ax.text(x = 0, y = 4, s = 'bloop', size=10, ha = 'left', va = 'top', wrap = True)
#ax.axis('off')
window = tk.Tk()
canvas = tk.Canvas(window, bg = 'white')
canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
rendered_latex = FigureCanvasTkAgg(fig, master = canvas)
rendered_latex.draw()
rendered_latex.get_tk_widget().place(relx = 0, rely = 0)

window.mainloop()
