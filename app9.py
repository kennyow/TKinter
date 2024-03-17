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

storage_variable = tk.StringVar()


option_one = ttk.Radiobutton(
    root,
    text = "Option 1",
    variable = storage_variable,
    value="First Option"
)
option_one.pack()

option_two = ttk.Radiobutton(
    root,
    text = "Option 2",
    variable = storage_variable,
    value="Second Option"
)
option_two.pack()

option_three = ttk.Radiobutton(
    root,
    text = "Option 3",
    variable = storage_variable,
    value="Third Option"
)
option_three.pack()
root.mainloop()