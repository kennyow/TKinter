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


selected_weekday = tk.StringVar()


weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
weekday["state"] = "readonly" #normal
weekday.pack()


def handle_selection(event):
    print("Today is", selected_weekday.get())
    print("But we're gonna change it to Friday")
    selected_weekday.set("Friday")
    print(weekday.current())

weekday.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()