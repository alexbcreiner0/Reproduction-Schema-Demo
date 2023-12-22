import tkinter as tk
from tkinter import filedialog #<--- useful!!!
import fitz  # PyMuPDF

class PDFViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.pdf_document = None

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open PDF", command=self.open_pdf)
        file_menu.add_command(label="Exit", command=root.destroy)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if file_path:
            self.load_pdf(file_path)

    def load_pdf(self, file_path):
        self.pdf_document = fitz.open(file_path)
        self.display_pdf_page(0)

    def display_pdf_page(self, page_number):
        if self.pdf_document:
            page = self.pdf_document[page_number]
            pix = page.get_pixmap()
            
            self.canvas.config(scrollregion=(0, 0, pix.width, pix.height))
            
            tk_img = tk.PhotoImage(data=pix.get_data("ppm"))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
            
            self.root.title(f"PDF Viewer - Page {page_number + 1}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFViewerApp(root)
    root.geometry("800x600")
    root.mainloop()
