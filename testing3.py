import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

window = ctk.CTk()
window.geometry('400x400')

checkbutton = ctk.CTkSwitch(window, text = '')
checkbutton.pack()

window.mainloop()