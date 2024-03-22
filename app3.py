import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

# Adicionando um separador preto e mais largo entre os widgets empacotados
ttk.Separator(main, orient='horizontal', bg='black', thickness=2).pack(fill='x')

tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill='both')
tk.Label(main, text="Label top", bg="blue").pack(side="top", expand=True, fill='both')

tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill='both')

root.mainloop()

