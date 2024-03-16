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


text = tk.Text(root, height=8)
text.pack()

text.insert("1.0", "Please enter a comment...") # O 1 é a posição que quer inserir o texto ( 1 - primeira linha, 0 - caractere)
#text["state"] = "disabled" #proibe a digitação
text["state"] = "normal"

text_content = text.get("1.0", "end")#começo e o fim
print(text_content)

root.mainloop()