import tkinter as tk
from tkinter import ttk #buttons, labels, etc


# Para melhoramento visual da janela criada
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def greet():
    print(f"IAEEEW, {user_name.get() or 'World'}!")

root = tk.Tk() #Creating a Tk object
root.title("MARSUPILAMI")

root.columnconfigure(0, weight = 1)

user_name = tk.StringVar() #Cria um placeholder

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column = 0, sticky="EW")

name_label = ttk.Label(input_frame,text="Nome: " )
name_label.grid(row=0, column = 0, padx=(0,10))

name_entry =ttk.Entry(input_frame,width = 15, textvariable= user_name) #width é a quantidade de caracteres
name_entry.grid(row=0, column = 1)
name_entry.focus()

buttons = ttk.Frame(root, padding=(20,10))
buttons.grid(row=1, column=0, sticky="EW") #East and West ficam presos

buttons.columnconfigure(0, weight = 1)
buttons.columnconfigure(1, weight = 1)

greet_button = ttk.Button(buttons, text="Aperta!", command=greet) #insere a aplicação princial root, command é a função que o botão exerce
#greet_button.pack() #Coloca o botão na janela ficando centralizado
#* Da forma que está, abre a janela com o botão, e o print aparece no terminal
greet_button.grid(row=0, column = 0, sticky="EW") #Coloca o botão na janela ficando à esquerda, fill preenche o espaço em branco com o botão por inteiro no eixo x, y ou os dois (both)(visível ao extender a janela utilizando expand)


#Acrescentando o botão quit
quit_button = ttk.Button(buttons, text="Sair", command=root.destroy) #destroy destrói o root
quit_button.grid(row=0, column = 1, sticky="EW")#Coloca o botão  Sair na janela, à esquerda
root.mainloop()