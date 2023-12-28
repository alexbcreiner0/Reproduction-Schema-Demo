import tkinter as tk
from matplotlib import pyplot as plt
import customtkinter as ctk
from PIL import Image, ImageTk
from matplotlib import rcParams
from main import EntryBlock

COLORS = {'dark_gray': '#242424','light_gray': '#2b2b2b', 'entry_gray': '#343638'}
rcParams['backend'] = 'TkAgg'

def resize_and_crop(image, pix_width, cropped_bbox = True):
    # resize
    ratio = image.size[0] / image.size[1]
    pix_height = int(pix_width / ratio)
    image = image.resize((pix_width, pix_height))
    # crop
    if cropped_bbox: 
        bbox = image.getbbox()
        new_bbox = (bbox[0]-5, bbox[1]-5, bbox[2], bbox[3])
        image = image.crop(new_bbox)
    return image

def latex_image(text, png_path, txt_color):
    fig = plt.figure()
    plt.axis('off')
    plt.text(x = 0.5, y = 0.5, s = f'{text}', size = 60, ha = 'center', va = 'center', color = 'black')
    plt.tight_layout(pad=0)
    plt.savefig(
        png_path,
        format = 'png', 
        bbox_inches = 'tight',
        pad_inches = 0,
        transparent = True)
    image = Image.open(png_path)
    return image

window = ctk.CTk()
window.geometry('1366x768')
window.columnconfigure(0, uniform = 'a')
window.rowconfigure((0,1), uniform = 'a')
window.rowconfigure(2, uniform = 'a', weight = 2)

frame_1 = ctk.CTkFrame(window, fg_color = 'transparent')
frame_2 = ctk.CTkFrame(window, fg_color = 'transparent')
frame_3 = ctk.CTkFrame(window, fg_color = 'transparent')
checkbutton_y1 = ctk.CTkCheckBox(frame_1, text = '')
checkbutton_y2 = ctk.CTkCheckBox(frame_2, text = '')

frame_1.grid(row = 0, column = 0, sticky = 'w', padx = 10)
frame_2.grid(row = 1, column = 0, sticky = 'w', padx = 10)
frame_3.grid(row = 2, column = 0)

image_y1 = latex_image("Match $y_1$ with $y_2$: ", "y_1", "white")
image_y1 = resize_and_crop(image_y1, 100)
image_y1_tk = ImageTk.PhotoImage(image_y1)
canvas_y1 = tk.Canvas(frame_1, width = image_y1.size[0], height = image_y1.size[1])
canvas_y1.create_image(0,0, image = image_y1_tk, anchor = 'nw')

image_y2 = latex_image("Match $y_2$ with $y_1$", "y_2", "white")
image_y2 = resize_and_crop(image_y2, 100)
image_y2_tk = ImageTk.PhotoImage(image_y2)
canvas_y2 = tk.Canvas(frame_2, width = image_y2.size[0], height = image_y2.size[1])
canvas_y2.create_image(0,0, image = image_y2_tk, anchor = 'nw')

entry_block_y1 = EntryBlock(frame_3, "$y_1= $", "hi", (0,5), 1)
entry_block_y1.grid(row = 2, column = 0)

canvas_y1.pack(side = 'left')
checkbutton_y1.pack(anchor = 'center', side = 'left')

canvas_y2.pack(side = 'left')
checkbutton_y2.pack(anchor = 'center')

window.mainloop()