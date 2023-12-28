import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget for displaying the input and result
        self.entry = tk.Entry(root, width=20, font=('Arial', 18), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons and add them to the grid
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, value):
        current_text = self.entry.get()

        if value == 'C':
            # Clear the entry
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                # Evaluate the expression and display the result
                result = str(eval(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                # Handle errors (e.g., division by zero)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            # Append the clicked button value to the entry
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
