import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

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
app_pessoa_linha = tk.Label(frame_cima, text="0", height=1, anchor="center",
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
app_pc_linha = tk.Label(frame_cima, text="0", height=1, anchor="center",
                         bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=250, y=0)

#pontuação pc
app_pc_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg = cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=185,y=20)

#barra de empate
app_empate = tk.Label(frame_cima, text="", width=255, anchor="center", bg=cor3,
                   fg=cor0, font=("Ivy 1 bold"))
app_empate.place(x=0, y=95)

janela.mainloop()

