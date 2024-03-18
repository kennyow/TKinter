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


def handle_scale_change(event):
    print(scale.get())


current_value = tk.DoubleVar()

scale = ttk.Scale(root, orient= "horizontal", from_=0, to=5, command=handle_scale_change, variable=current_value)
scale.pack(fill="x")

#scale["state"] = "disabled"

root.mainloop()

print(current_value.get())