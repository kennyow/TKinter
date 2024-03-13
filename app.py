import tkinter as tk
from tkinter import ttk #buttons, labels, etc



def greet():
    print("IAEEEW!")

root = tk.Tk() #Creating a Tk object

greet_button = ttk.Button(root, text="Aperta!", command=greet) #insere a aplicação princial root, command é a função que o botão exerce
#greet_button.pack() #Coloca o botão na janela ficando centralizado
#* Da forma que está, abre a janela com o botão, e o print aparece no terminal
greet_button.pack(side='left', fill='both', expand=True) #Coloca o botão na janela ficando à esquerda, fill preenche o espaço em branco com o botão por inteiro no eixo x(visível ao extender a janela utilizando expand)


#Acrescentando o botão quit
quit_button = ttk.Button(root, text="Sair", command=root.destroy) #destroy destrói o root
quit_button.pack(side='left', fill='y')#Coloca o botão  Sair na janela, à esquerda
root.mainloop()