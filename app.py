import tkinter as tk
from tkinter import ttk #buttons, labels, etc



def greet():
    print(f"IAEEEW, {user_name.get() or 'World'}!")

root = tk.Tk() #Creating a Tk object

user_name = tk.StringVar() #Cria um placeholder

name_label = ttk.Label(root,text="Nome: " )
name_label.pack(side="left", padx=(0,10))

name_entry =ttk.Entry(root,width = 15, textvariable= user_name) #width é a quantidade de caracteres
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="Aperta!", command=greet) #insere a aplicação princial root, command é a função que o botão exerce
#greet_button.pack() #Coloca o botão na janela ficando centralizado
#* Da forma que está, abre a janela com o botão, e o print aparece no terminal
greet_button.pack(side='left', fill='both', expand=True) #Coloca o botão na janela ficando à esquerda, fill preenche o espaço em branco com o botão por inteiro no eixo x, y ou os dois (both)(visível ao extender a janela utilizando expand)


#Acrescentando o botão quit
quit_button = ttk.Button(root, text="Sair", command=root.destroy) #destroy destrói o root
quit_button.pack(side='left', fill='both', expand=True)#Coloca o botão  Sair na janela, à esquerda
root.mainloop()