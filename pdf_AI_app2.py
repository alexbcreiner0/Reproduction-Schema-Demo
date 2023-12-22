import tkinter as tk
from PIL import Image, ImageTk
import fitz

window = tk.Tk()

canvas = tk.Canvas(window)
pdf_path = r"C:\Users\creiner\Documents\Means of Production\My Latex Notes\Circuits and Switching Lemma.pdf"
pdf = fitz.open(pdf_path)
page = pdf[0]
pix = page.get_pixmap()

image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
print(pix.width, pix.height)
img_width, img_height = pix.width, pix.height
tk_image = ImageTk.PhotoImage(image = image)

canvas.create_image(0,0,anchor = 'nw', image = tk_image)
window.geometry(f'{img_width}x{img_height}')
#scrollbar = tk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
#scrollbar.pack(side = 'right', fill = 'y')
#canvas.config(scrollregion = (0,0, img_width, img_height), yscrollcommand = scrollbar.set)
canvas.config(scrollregion = (0,0, img_width, img_height))
canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

window.mainloop()