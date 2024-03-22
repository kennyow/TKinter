import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness
import tkinter.font as font

set_dpi_awareness()

# Root Window
root = tk.Tk()

#Title
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

#Values
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")


#Function to calculate feet:
def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f} ")

    except ValueError:
        pass


root.columnconfigure(0, weight=1)
main = ttk.Frame(root, padding=(30, 15))
main.grid()

#Name Metres
metres_label = ttk.Label(main, text = "Metres: ")
metres_label.grid(column=0, row=0, sticky="w")

#Input
metres_input = ttk.Entry(main, width = 10, textvariable=metres_value, font=("Segoe UI", 15))
metres_input.grid(column=1, row=0, sticky="ew")
metres_input.focus()

#Name Feet
feet_label = ttk.Label(main, text="Feet:")
feet_label.grid(column=0, row=1, sticky="w")

#Display
feet_display = ttk.Label(main, textvariable=feet_value)
feet_display.grid(column=1, row = 1, sticky="ew")


#Calculate
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)
calc_button.grid(column=0, row=2, columnspan=2, sticky="ew")

#Put pads and pady on all grids
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)



root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
root.mainloop()

