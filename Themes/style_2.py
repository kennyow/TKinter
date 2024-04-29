import tkinter as tk
from tkinter import ttk


root = tk.Tk()


# Create it after instead
style = ttk.Style(root)  # Pass in which application this style is for.


# Get the themes available in your system
name = ttk.Label(root, text = "hello, world!")
name.pack()

print(style.layout("TLabel")) 

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.theme_use("clam")

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.configure("TLabel", bordercolor = '#f00')
style.configure("TLabel", borderwidth = 20)
style.configure("TLabel", relief="solid")


root.mainloop()