import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import main
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# def make_fig(text, master):
# 	fig, ax = plt.subplots()
# 	plt.axis('off')
# 	plt.text(x = 0.5, y = 0.5, s = f'{text}', size = 10, ha = 'center')
# 	canvas = FigureCanvasTkAgg(fig, master = master)
# 	return canvas

window = ctk.CTk()
window.columnconfigure((0,1), uniform = 'a')
window.rowconfigure(0, uniform = 'a')

frame_y1 = ctk.CTkFrame(window)
frame_y2 = ctk.CTkFrame(window)

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get the window width and height
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()

# Calculate DPI
dpi = screen_width / (window_width / 2.54)
plt.rcParams['figure.dpi'] = dpi

checkbutton_y1 = ctk.CTkSwitch(frame_y1, text = '')
checkbutton_y2 = ctk.CTkSwitch(frame_y2, text = '')

label_image_ctk_y1 = main.get_ctk_image('Match $y_2$', 'y2_balanced', size = 15)
label_image_ctk_y2 = main.get_ctk_image('Match $y_2$', 'y2_balanced', size = 5)
label_y1 = ctk.CTkLabel(frame_y1, text = '', fg_color = ('#CFCFCF', '#333333'), image = label_image_ctk_y1)
label_y2 = ctk.CTkLabel(frame_y2, text = '', fg_color = ('#CFCFCF', '#333333'), image = label_image_ctk_y2)

#label_y1.pack(fill = 'both')
label_y1.pack(fill = 'both', expand = True)
checkbutton_y1.pack()
#place(relx = 0.3, rely = 0, relwidth = 1, relheight = 0.4)
label_y2.pack()
checkbutton_y2.pack()
#place(relx = 0.3, rely = 0, relwidth = 1, relheight = 0.4)

frame_y1.grid(row = 0, column = 0)
frame_y2.grid(row = 0, column = 1)


window.mainloop()