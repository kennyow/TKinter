import tkinter as tk
from tkinter import ttk


root = tk.Tk()


# Create it after instead
style = ttk.Style(root)  # Pass in which application this style is for.


style.theme_use("clam")
#Changing the color of the name after pressed/ passing the cursor the name becomes white
style.map("CustomButton.TButton",
          foreground=[("pressed", "red"), ("active", "white")],
          background=[("pressed", "!disabled", "black"), ("active", "black")],
          font=[("pressed", ("TKDefaultFont", 15))])



# Get the themes available in your system
name = ttk.Label(root, text = "hello, world!")
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text = "Press me.", style = "CustomButton.TButton")
name.pack()
entry.pack()
button.pack()

root.mainloop()