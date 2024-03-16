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

greeting = tk.StringVar()

label = ttk.Label(root, padding=10, textvariable=greeting)
label.pack()

greeting.set("Hello, John")




'''main =ttk.Frame(root) #Criando um frame para caber os botões
main.pack(side="left", fill="both", expand=True )


tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill='both') #Fill x faz com que o retângulo preencha todo o espaço da largura
tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill='both') 
tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill='both') '''
root.mainloop()