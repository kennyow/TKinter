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

programming_languages = ('Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'Swift', 'Go')


initial_value = tk.StringVar(value=20)
spin_box = tk.Spinbox(master=
                      
                      
    root,
    #from_=0,
    #to=10,
    values=(5,10, 55, 123),
    textvariable=initial_value,
    wrap=False
    )

spin_box.pack()


print(spin_box.get())


root.mainloop()