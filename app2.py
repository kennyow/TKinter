import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Retângulo 1", bg="green", fg="white") #fg cor da letra, bg cor de fundo
rectangle_1.pack(ipadx=10, ipady=10, fill='both', expand=True) #Fill x faz com que o retângulo preencha todo o espaço da largura

rectangle_2 = tk.Label(root, text="Retângulo 2", bg="red", fg="white") #fg cor da letra, bg cor de fundo
rectangle_2.pack(ipadx=10, ipady=10, expand=True)

root.mainloop()