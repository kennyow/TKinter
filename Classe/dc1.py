import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness
import tkinter.font as font

set_dpi_awareness()



class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        ttk.Label(self, text="Hello, World!").pack()


root = HelloWorld()

root.mainloop()

