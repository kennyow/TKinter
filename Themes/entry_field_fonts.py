import tkinter as tk
from tkinter import ttk
import tkinter.font as font


root = tk.Tk()
style = ttk.Style(root)  # Pass in which application this style is for.
print(font.families()) #show the fonts in the system
#font.nametofont("TkDefaultFont").configure(size=15)
warningLabelFont = font.Font(family="Helvetica", size = 14, weight ="bold")

# Get the themes available in your system
name = ttk.Label(root, text = "hello, world!", font=warningLabelFont)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me.")
name.pack()
entry.pack()
button.pack()



root.mainloop()