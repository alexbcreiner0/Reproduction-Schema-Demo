from main import EntryBlock
import tkinter as tk
import customtkinter as ctk

window = ctk.CTk()

entry_block = EntryBlock(window, "hi", "hi", (0,5), 1)
entry_block.pack()

window.mainloop()