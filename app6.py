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

text = tk.Text(root, height = 9)
text.grid(row = 0, column = 0, sticky="ew")

text.insert("1.0", "Please enter a comment...") # O 1 é a posição que quer inserir o texto ( 1 - primeira linha, 0 - caractere)

text_scroll = ttk.Scrollbar(root, orient="vertical", command="text.yview")
text_scroll.grid(row=0, column=1, sticky = "ns") #north to south
text["yscrollcommand"] = text_scroll.set



root.mainloop()