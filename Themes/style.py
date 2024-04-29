import tkinter as tk
from tkinter import ttk


root = tk.Tk()


# Create it after instead
style = ttk.Style(root)  # Pass in which application this style is for.


# Get the themes available in your system
name = ttk.Label(root, text = "hello, world!")
entry = ttk.Entry(root, width=15)
name.pack()

#print(name["style"]) #default
#print(name.winfo_class()) #Tlabel style check


style.configure("TLabel", font=("Segoe UI", 20))
root.mainloop()