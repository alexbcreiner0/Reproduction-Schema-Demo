import tkinter as tk

def show_info(event):
    global info_window
    info_text = "This is additional information!"
    
    # Close existing info_window if it exists
    if info_window:
        info_window.destroy()

    info_window = tk.Toplevel(root)
    info_window.title("Information")
    
    # Position the info window near the cursor
    x, y = event.x_root + 10, event.y_root + 10
    info_window.geometry(f"+{x}+{y}")
    
    label = tk.Label(info_window, text=info_text, padx=10, pady=10)
    label.pack()

def on_enter(event):
    question_mark_button.config(bg="lightgray")
    show_info(event)

def on_leave(event):
    question_mark_button.config(bg="SystemButtonFace")
    
    # Close the info_window when the mouse leaves the button
    if info_window:
        info_window.destroy()

# Create the main window
root = tk.Tk()
root.title("Question Mark GUI")

# Global variable to store the info_window reference
info_window = None

# Create a question mark button
question_mark_button = tk.Button(root, text="?", width=3, height=2)
question_mark_button.grid(row=0, column=0, padx=10, pady=10)

# Bind events to the question mark button
question_mark_button.bind("<Enter>", on_enter)
question_mark_button.bind("<Leave>", on_leave)

# Start the Tkinter event loop
root.mainloop()
