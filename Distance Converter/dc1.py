import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

# Root Window
root = tk.Tk()

#Title
root.title("Distance Converter")

root.columnconfigure(0, weight=1)
main = ttk.Frame(root, padding=(30, 15))
main.grid()

metres_label = ttk.Label(main, text = "Metres: ")
metres_input = ttk.Entry(main, width = 10)
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet shown here")
calc_button = ttk.Button(main, text="Calculate")

metres_label.grid(column=0, row=0, sticky="w", padx=5, pady = 5)
metres_input.grid(column=1, row=0, sticky="ew", padx=5, pady = 5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="w", padx=5, pady = 5)
feet_display.grid(column=1, row = 1, sticky="ew", padx=5, pady = 5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="ew", padx=5, pady = 5)

root.mainloop()

