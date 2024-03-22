import tkinter as tk
from tkinter import ttk #buttons, labels, etc
from PIL import Image, ImageTk
from windows import set_dpi_awareness


# Para melhoramento visual da janela criada
set_dpi_awareness()

def greet():
    print(f"Aluno, {user_name.get() or 'World'}!")

#* OBJETO TK
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)

#*Título
root.title("LUIZ AUGUSTO CRISPIM")

root.columnconfigure(3, weight = 0)

user_name = tk.StringVar() #Cria um placeholder

selected_weekday = tk.StringVar()


input_frame = ttk.Frame(root, padding=(20, 10, 20, 0), borderwidth=2, relief='solid')
input_frame.grid(row=0, sticky="EW")

#*NOME TURMAS
nome_turmas = ttk.Label(input_frame,text="TURMAS:")
nome_turmas.grid(row=0, column = 0, padx=(0,10)) #padx= distância do nome TURMAS

#* COMBOBOX TURMAS
turmas = ttk.Combobox(input_frame, textvariable=selected_weekday)
turmas["values"] = ('1 ANO A', '1 ANO B', '1 ANO C', '1 ANO D', '2 ANO A', '2 ANO B', '2 ANO C')
turmas["state"] = "readonly" #normal
turmas.grid(row=0, column = 1, padx=(0,10))

#* NOME ALUNOS
nome_aluno = ttk.Label(input_frame,text="NOME: ")
nome_aluno.grid(row=0, column = 3, padx=(0,10)) #padx= distância do nome TURMAS



name_entry =ttk.Entry(input_frame, width = 30, textvariable= user_name) #width é a quantidade de caracteres
name_entry.grid(row=0, column = 4)
name_entry.focus()

buttons = ttk.Frame(root, padding=(20,10), borderwidth=2, relief='solid')
buttons.grid(row=1, column=3, sticky="EW") #East and West ficam presos

text = tk.Text(input_frame, height=8, width=8)
text.grid(row=2, column=0, )

buttons.columnconfigure(0, weight = 1)
buttons.columnconfigure(1, weight = 1)


#* BOTÕES
greet_button = ttk.Button(buttons, text="Aperta!", command=greet) #insere a aplicação princial root, command é a função que o botão exerce
#greet_button.pack() #Coloca o botão na janela ficando centralizado
#* Da forma que está, abre a janela com o botão, e o print aparece no terminal
greet_button.grid(row=11, column = 3, sticky="EW",) #Coloca o botão na janela ficando à esquerda, fill preenche o espaço em branco com o botão por inteiro no eixo x, y ou os dois (both)(visível ao extender a janela utilizando expand)


#Acrescentando o botão quit
quit_button = ttk.Button(buttons, text="Sair", command=root.destroy) #destroy destrói o root
quit_button.grid(row=12, column = 3, sticky="EW")#Coloca o botão  Sair na janela, à esquerda
root.mainloop()