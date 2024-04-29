import tkinter as tk
from tkinter import ttk


root = tk.Tk()


# Create it after instead
style = ttk.Style(root)  # Pass in which application this style is for.

#Create the style
style.configure("CustomEntryStyle.TEntry", padding = 20)

# Get the themes available in your system
name = ttk.Label(root, text = "hello, world!")
entry = ttk.Entry(root, width=15)
#Using the created style
entry["style"] = "CustomEntryStyle.TEntry"
name.pack()
entry.pack()


root.mainloop()