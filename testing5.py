import customtkinter as ctk
import tkinter as tk

def do_thing(*args): 
	print(args)
	#print(type(var.get()))

window = ctk.CTk()

var = tk.BooleanVar(value = True)
var.trace_add('write', do_thing)
switch = ctk.CTkSwitch(window, text = 'press me', variable = var)
switch.pack()

window.mainloop()