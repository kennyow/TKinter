import tkinter as tk
from tkinter import ttk  # buttons, labels, etc
from PIL import Image, ImageTk

# Para melhoramento visual da janela criada
def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

set_dpi_awareness()

def greet():
    print(f"Aluno, {user_name.get() or 'World'}!")

# OBJETO TK
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)

# Título
root.title("LUIZ AUGUSTO CRISPIM")

# Configurando a geometria do layout
root.columnconfigure(0, weight=1)  # Coluna que ocupa todo o espaço disponível

user_name = tk.StringVar()  # Cria um placeholder
selected_weekday = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 10), borderwidth=4, relief='solid')
input_frame.grid(row=0, sticky="EW")

# NOME TURMAS
nome_turmas = ttk.Label(input_frame, text="TURMAS:")
nome_turmas.grid(row=0, column=0, padx=(0, 10))  # padx= distância do nome TURMAS

# COMBOBOX TURMAS
turmas = ttk.Combobox(input_frame, textvariable=selected_weekday)
turmas["values"] = ('1 ANO A', '1 ANO B', '1 ANO C', '1 ANO D', '2 ANO A', '2 ANO B', '2 ANO C')
turmas["state"] = "readonly"  # normal
turmas.grid(row=0, column=1, padx=(0, 10))

# NOME ALUNOS
nome_aluno = ttk.Label(input_frame, text="NOME: ")
nome_aluno.grid(row=0, column=3, padx=(0, 10))  # padx= distância do nome TURMAS

# CAIXA NOME ALUNOS
name_entry = ttk.Entry(input_frame, width=30, textvariable=user_name)  # width é a quantidade de caracteres
name_entry.grid(row=0, column=4, padx=(0, 10), sticky="EW")
name_entry.focus()

# LOGO JUVE
image = Image.open("C:\\Users\\kenny\\Documents\\Projeto Python\\Tkinter\\aaroma.png")  # Substitua o caminho pela localização da sua imagem
image = image.resize((40, 40), Image.ANTIALIAS)  # Redimensionando a imagem conforme necessário
photo = ImageTk.PhotoImage(image)

image_label = ttk.Label(input_frame, image=photo)
image_label.grid(row=0, column=6, rowspan=2, padx=(10, 0), sticky="E")  # Alinhado à direita (East)

# Novo Frame à Esquerda
new_frame = ttk.Frame(root, padding=(20, 10, 20, 10), borderwidth=4, relief='solid')
new_frame.grid(row=1, column=0, sticky="W")

# Widgets no Novo Frame
label_new_frame = ttk.Label(new_frame, text="NOMES")
label_new_frame.grid(row=0, column=0, padx=(100, 0))

#* Caixa de TEXTO
text = tk.Text(new_frame, height=22, width=45)
text.grid(row=1, column=0, columnspan=5 , sticky="W")



# Novo Frame à Direita
new_frame = ttk.Frame(root, padding=(20, 10, 20, 10), borderwidth=4, relief='solid')
new_frame.grid(row=1, column=0, sticky="E")

# Widgets no Novo Frame
label_new_frame = ttk.Label(new_frame, text="AÇÕES")
label_new_frame.grid(row=0, column=0, padx=(0, 10))

# Botões no Novo Frame
button_new_frame = ttk.Button(new_frame, text="MATRÍCULA")
button_new_frame.grid(row=1, column=0, padx=(0, 10), pady=(20,0))

# Outro Botão no Novo Frame
button2_new_frame = ttk.Button(new_frame, text="DECLARAÇÃO")
button2_new_frame.grid(row=2, column=0, padx=(0, 10), pady=(20,0))

# Outro Botão no Novo Frame
button3_new_frame = ttk.Button(new_frame, text="TRANSFERÊNCIA")
button3_new_frame.grid(row=3, column=0, padx=(0, 10), pady=(20,0))


root.mainloop()
