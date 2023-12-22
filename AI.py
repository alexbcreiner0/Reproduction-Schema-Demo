import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def update_graph(*args):
    try:
        # Get the parameter value from the entry widget
        parameter_value = float(entry_var.get())
        
        # Generate x values
        x = np.linspace(-10, 10, 100)
        
        # Define the function (e.g., a simple quadratic function)
        y = x**2 + parameter_value
        
        # Clear the previous plot
        ax.clear()
        
        # Plot the new function
        ax.plot(x, y)
        
        # Set labels and title
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title(f'Graph of x^2 + {parameter_value}')
        
        # Update the canvas
        canvas.draw()
    except ValueError:
        pass

# Create the main window
root = tk.Tk()
root.title("Function Graph Plotter")

# Create a StringVar to store the entry widget value
entry_var = tk.StringVar()

# Create a label and entry widget for the parameter
parameter_label = ttk.Label(root, text="Enter Parameter:")
parameter_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

parameter_entry = ttk.Entry(root, textvariable=entry_var)
parameter_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
entry_var.trace_add("write", update_graph)

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Initial graph with a default parameter value
update_graph()

# Run the Tkinter event loop
root.mainloop()