import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

# Root Window
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)

#Title
root.title("Widget Examples")

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

ttk.Label(root, text="Manchester United", padding=20).pack()
ttk.Separator(root, orient="horizontal").pack(fill="x") #preenche em preto o eixo x

ttk.Label(root, text="Liverpool", padding=20).pack()



root.mainloop()