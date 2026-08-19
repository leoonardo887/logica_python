import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import random
#pip install pillow
from PIL import Image, ImageTk

# Cores
cor0 = "#FFFFFF"  # branco
cor1 = "#333333"  # preto
cor2 = "#fcc058"  # laranja
cor3 = "#fff873"  # amarelo
cor4 = "#34eb3d"  # verde
cor5 = "#e85151"  # vermelho
fundo = "#3b3b3b"


janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)


frame_cima = tk.Frame(
    janela,
    width=260,
    height=100,
    bg=cor1,
    relief="raised"
)
frame_cima.grid(row=0, column=0, sticky=tk.NW)


frame_baixo = tk.Frame(
    janela,
    width=260,
    height=300,
    bg=cor0,
    relief="flat"
)
frame_baixo.grid(row=1, column=0, sticky=tk.NW)

estilo= ttk.Style(janela)
estilo.theme_use("clam")

#configurando os jogadores
#jogador pessoa
app_pessoa = tk.Label(frame_cima, text="jogador", height=1, anchor="center",
                   bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)

#barra marcou pontos
app_pessoa_linha = tk.Label(frame_cima, text="", height=10, anchor="center",
                         bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)

#pontuação
app_pessoa_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg = cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50,y=20)

#separação da pontuação
app_vs = tk.Label(frame_cima, text=":", height=1, anchor="center",
               bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125,y=20)


#jogador pc
app_pc = tk.Label(frame_cima, text="PC", height=1, anchor="center",
                  bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc.place(x=185, y=70)

#barra marcou pontos pc
app_pc_linha = tk.Label(frame_cima, text="", height=10, anchor="center",
                         bg=cor5, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)

#pontuação pc
app_pc_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg = cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=185,y=20)

#barra de empate
app_empate = tk.Label(frame_cima, text="", width=255, anchor="center", bg=cor3,
                   fg=cor0, font=("Ivy 1 bold"))
app_empate.place(x=0, y=95)

#mostra a jogada do pc
app_jogada_pc = tk.Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pc.place(x=190, y=10)

#mostra a jogada do jogador
app_jogada_pessoa = tk.Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pessoa.place(x=10, y=10)

app_vencedor = tk.Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))

#função de iniciar jogo.
def iniciar_jogo():
    global icone_pedra
    global icone_papel
    global icone_tesoura
    global btn_papel
    global btn_pedra
    global btn_tesoura
    global escolha_pessoa
    global escolha_pc
    global pontos_pessoa
    global pontos_pc
    global rodadas
    pontos_pessoa = 0
    pontos_pc = 0
    rodadas = 5

    app_pessoa_pontos["text"] = 0
    app_pc_pontos["text"] = 0

    app_vencedor["text"] = ""
    app_jogada_pessoa["text"] = ""
    app_jogada_pc["text"] = ""

global escolha_pessoa
global escolha_pc
global pontos_pessoa
global pontos_pc
global rodadas
pontos_pessoa = 0
pontos_pc = 0
rodadas = 5

def testa_empate(escolha_pessoa, escolha_pc):
    return escolha_pessoa == escolha_pc

def testa_vitoria_pessoa(escolha_pessoa, escolha_pc):
    if escolha_pessoa == "pedra" and escolha_pc == "tesoura" or escolha_pessoa == "papel" and escolha_pc == "pedra" or escolha_pessoa == "tesoura" and escolha_pc == "papel":
        return True
    return False

def testa_vitoria_pc(escolha_pessoa, escolha_pc):
    if escolha_pc == "pedra" and escolha_pessoa == "tesoura" or escolha_pc == "papel" and escolha_pessoa == "pedra" or escolha_pc == "tesoura" and escolha_pessoa == "papel":
        return True
    return False

def terminar_jogo():
    if pontos_pessoa > pontos_pc:
        print("Pessoa ganhou!")
        msg_pessoa_ganhou = tk.Label(frame_baixo, text="Você ganhou!", height=1, anchor="center", bg= cor0, fg=cor1, font=("Ivy 10 bold"))
        msg_pessoa_ganhou.place(x=80, y=20)
    elif pontos_pc > pontos_pessoa:
        print("Você perdeu!")
        msg_pessoa_perdeu = tk.Label(frame_baixo, text="Você perdeu!", height=1, anchor="center", bg= cor0, fg=cor1, font=("Ivy 10 bold"))
        msg_pessoa_perdeu.place(x=80, y=20)
    else:
        ("Empate.")
        msg_pessoa_empatou = tk.Label(frame_baixo, text="Empate!", height=1, anchor="center", bg= cor0, fg=cor1, font=("Ivy 10 bold"))
        msg_pessoa_empatou.place(x=95, y=20)

#função das jogadas
def jogar(jogada):
    global pontos_pessoa
    global pontos_pc    
    global rodadas
    opcoes = ["pedra", "papel", "tesoura"]

    app_pessoa_linha["bg"] = cor1
    app_pc_linha["bg"] = cor1
    app_empate["bg"] = cor1

    if rodadas > 0:
        print(rodadas)
        escolha_pc = random.choice(opcoes)
        escolha_pessoa = jogada
        app_jogada_pc["text"] = escolha_pc

        escolha_pessoa = jogada
        app_jogada_pessoa["text"] = escolha_pessoa
        print(escolha_pessoa, escolha_pc)
        rodadas -= 1

        #caso empate
        if testa_empate(escolha_pessoa, escolha_pc):
            app_empate["bg"] = cor3
        elif testa_vitoria_pessoa(escolha_pessoa, escolha_pc):
            pontos_pessoa += 10
            app_pessoa_pontos["text"] = pontos_pessoa
            app_pessoa_linha["bg"] = cor2
        elif testa_vitoria_pc(escolha_pessoa, escolha_pc):
            pontos_pc += 10
            app_pc_pontos["text"] = pontos_pc
            app_pc_linha["bg"] = cor2

        #mostrar pontos
    else:
        terminar_jogo()

icone_pedra = Image.open("Pedra.png")
icone_pedra = icone_pedra.resize((50, 50), Image.LANCZOS)
icone_pedra = ImageTk.PhotoImage(icone_pedra)
btn_pedra = tk.Button(frame_baixo, command=lambda: jogar("pedra"), width=50, height=50, image=icone_pedra,
                   bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_pedra.place(x=170, y=55)

icone_papel = Image.open("Papel.png")
icone_papel = icone_papel.resize((50, 50), Image.LANCZOS)
icone_papel = ImageTk.PhotoImage(icone_papel)
btn_papel = tk.Button(frame_baixo,command=lambda: jogar("papel"), width=50, height=50, image=icone_papel,
                   bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_papel.place(x=40, y=50)

icone_tesoura = Image.open("Tesoura.png")
icone_tesoura = icone_tesoura.resize((50, 50), Image.LANCZOS)
icone_tesoura = ImageTk.PhotoImage(icone_tesoura)
btn_tesoura = tk.Button(frame_baixo,command=lambda: jogar("tesoura"), width=50, height=50, image=icone_tesoura,
                   bg=cor0, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_tesoura.place(x=110, y=50)

btn_reiniciar = tk.Button(frame_baixo,text="jogar",command=iniciar_jogo, width=30, height= 1, bg=cor1, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_reiniciar.place(x=5,y=110)

btn_sair = tk.Button(frame_baixo,text="Sair",command=quit, width=30, height= 1, bg=cor1, fg=cor0, compound="center", font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_sair.place(x=5,y=140)

janela.mainloop()