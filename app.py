import tkinter as tk
from tkinter import ttk #buttons, labels, etc


root = tk.Tk() #Creating a Tk object

#Create a Label
#ttk.Label(root, text="Bora, doido!").pack() #The label will be placed inside the root. Pack puts the elements into the window
ttk.Label(root, text="Bora, doido!", padding=(60,50)).pack() #(width, height)

root.mainloop()