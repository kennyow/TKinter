from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela() #Chama a função tela
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop() #Loop para a janela não fechar. Loop for the window not to close.

    def tela(self): # Para as configurações da tela. For screen's configuration
        self.root.title("Cadastro de Alunos") #Cria o título. Create the title
        self.root.configure(background='#4682B4') #Cor de fundo. Background color. 
        self.root.geometry('700x500') #Dimensões da janela. Window's dimensions
        self.root.resizable(True, True) #Tela responsiva. Responsive window
        self.root.maxsize(width=900, height=700) #Inicia com um tamanho máximo. Starts with maximun size
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self): #Criando quadros na tela. Create frames in the screen
        self.frame_1 = Frame(self.root, bd=4, bg='#98FB98', 
                             highlightbackground='#FF0000',
                             highlightthickness=3) #bd=border
        self.frame_1.place(relx = 0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#98FB98', 
                             highlightbackground='#FF0000',
                             highlightthickness=3) #bd=border
        self.frame_2.place(relx = 0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def criando_botoes(self):
        #* BOTÃO LIMPAR
        self.bt_limpar = Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
         #* BOTÃO BUSCAR
        self.bt_buscar = Button(self.frame_1, text="Buscar")
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        #* BOTÃO NOVO
        self.bt_novo = Button(self.frame_1, text="Novo")
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        #* BOTÃO ALTERAR
        self.bt_alterar = Button(self.frame_1, text="Alterar")
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        #* BOTÃO APAGAR
        self.bt_apagar = Button(self.frame_1, text="Apagar")
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
Application() #Chamando a classe para gerar o loop na janela. Calling Class to get the loop in the window