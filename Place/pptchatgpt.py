import tkinter as tk
import tkinter.ttk as ttk
import random

# pip install pillow
from PIL import Image, ImageTk

# CORES
cor0 = "#FFFFFF"  # branco
cor1 = "#333333"  # preto
cor2 = "#fcc058"  # laranja
cor3 = "#fff873"  # amarelo
cor4 = "#34eb3d"  # verde
cor5 = "#e85151"  # vermelho
fundo = "#3b3b3b"

# JANELA
janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)

# FRAMES
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


# Estilo
estilo = ttk.Style(janela)
estilo.theme_use("clam")

# JOGADOR
app_pessoa = tk.Label(
    frame_cima,
    text="jogador",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold")
)
app_pessoa.place(x=10, y=70)


# Barra do jogador
app_pessoa_linha = tk.Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor4,
    fg=cor0,
    font=("Ivy 10 bold")
)
app_pessoa_linha.place(x=0, y=0)


# Pontuação do jogador
app_pessoa_pontos = tk.Label(
    frame_cima,
    text="0",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)
app_pessoa_pontos.place(x=50, y=20)

# VS
app_vs = tk.Label(
    frame_cima,
    text=":",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)
app_vs.place(x=125, y=20)

# PC
app_pc = tk.Label(
    frame_cima,
    text="PC",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold")
)
app_pc.place(x=185, y=70)


# Barra do PC
app_pc_linha = tk.Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor5,
    fg=cor0,
    font=("Ivy 10 bold")
)
app_pc_linha.place(x=255, y=0)


# Pontuação do PC
app_pc_pontos = tk.Label(
    frame_cima,
    text="0",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)
app_pc_pontos.place(x=185, y=20)


# Barra de empate
app_empate = tk.Label(
    frame_cima,
    text="",
    width=255,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 1 bold")
)
app_empate.place(x=0, y=95)


# JOGADAS

# Jogada do PC
app_jogada_pc = tk.Label(
    frame_baixo,
    text="",
    height=1,
    anchor="center",
    bg=cor0,
    fg=cor1,
    font=("Ivy 10 bold")
)
app_jogada_pc.place(x=190, y=10)


# Jogada do jogador
app_jogada_pessoa = tk.Label(
    frame_baixo,
    text="",
    height=1,
    anchor="center",
    bg=cor0,
    fg=cor1,
    font=("Ivy 10 bold")
)
app_jogada_pessoa.place(x=10, y=10)


# Mensagem do vencedor
app_vencedor = tk.Label(
    frame_baixo,
    text="",
    height=1,
    anchor="center",
    bg=cor0,
    fg=cor1,
    font=("Ivy 10 bold")
)

# VARIÁVEIS DO JOGO
pontos_pessoa = 0
pontos_pc = 0
rodadas = 5

# INICIAR / REINICIAR JOGO
def iniciar_jogo():
    global pontos_pessoa
    global pontos_pc
    global rodadas

    pontos_pessoa = 0
    pontos_pc = 0
    rodadas = 5

    # Zera pontuação
    app_pessoa_pontos["text"] = "0"
    app_pc_pontos["text"] = "0"

    # Limpa jogadas
    app_jogada_pessoa["text"] = ""
    app_jogada_pc["text"] = ""

    # Limpa mensagem
    app_vencedor["text"] = ""
    app_vencedor.place_forget()

    # Reseta as barras
    app_pessoa_linha["bg"] = cor4
    app_pc_linha["bg"] = cor5
    app_empate["bg"] = cor1

# TESTA EMPATE
def testa_empate(escolha_pessoa, escolha_pc):
    return escolha_pessoa == escolha_pc

# TESTA VITÓRIA DO JOGADOR
def testa_vitoria_pessoa(escolha_pessoa, escolha_pc):

    if (
        escolha_pessoa == "pedra" and escolha_pc == "tesoura"
        or escolha_pessoa == "papel" and escolha_pc == "pedra"
        or escolha_pessoa == "tesoura" and escolha_pc == "papel"
    ):
        return True

    return False

# TESTA VITÓRIA DO PC
def testa_vitoria_pc(escolha_pessoa, escolha_pc):

    if (
        escolha_pc == "pedra" and escolha_pessoa == "tesoura"
        or escolha_pc == "papel" and escolha_pessoa == "pedra"
        or escolha_pc == "tesoura" and escolha_pessoa == "papel"
    ):
        return True

    return False


# TERMINAR JOGO
def terminar_jogo():

    if pontos_pessoa > pontos_pc:
        mensagem = "Você ganhou!"
        print("Pessoa ganhou!")

    elif pontos_pc > pontos_pessoa:
        mensagem = "Você perdeu!"
        print("Você perdeu!")

    else:
        mensagem = "Empate!"
        print("Empate!")

    app_vencedor["text"] = mensagem
    app_vencedor.place(x=80, y=20)


# JOGAR
def jogar(jogada):

    global pontos_pessoa
    global pontos_pc
    global rodadas

    opcoes = ["pedra", "papel", "tesoura"]

    # Não permite jogar depois das 5 rodadas
    if rodadas <= 0:
        return

    # Reseta as barras da rodada
    app_pessoa_linha["bg"] = cor1
    app_pc_linha["bg"] = cor1
    app_empate["bg"] = cor1

    # Escolha aleatória do PC
    escolha_pc = random.choice(opcoes)

    # Escolha do jogador
    escolha_pessoa = jogada

    # Mostra as jogadas
    app_jogada_pc["text"] = escolha_pc
    app_jogada_pessoa["text"] = escolha_pessoa

    print("Jogador:", escolha_pessoa)
    print("PC:", escolha_pc)

    # Diminui uma rodada
    rodadas -= 1

    print("Rodadas restantes:", rodadas)

    # EMPATE
    if testa_empate(escolha_pessoa, escolha_pc):

        app_empate["bg"] = cor3

    # JOGADOR GANHOU
    elif testa_vitoria_pessoa(escolha_pessoa, escolha_pc):

        pontos_pessoa += 10

        app_pessoa_pontos["text"] = pontos_pessoa
        app_pessoa_linha["bg"] = cor2

    # PC GANHOU
    elif testa_vitoria_pc(escolha_pessoa, escolha_pc):

        pontos_pc += 10

        app_pc_pontos["text"] = pontos_pc
        app_pc_linha["bg"] = cor2

    # TERMINOU AS 5 RODADAS

    if rodadas == 0:
        terminar_jogo()

# IMAGENS
icone_pedra = Image.open("Pedra.png")
icone_pedra = icone_pedra.resize((50, 50), Image.LANCZOS)
icone_pedra = ImageTk.PhotoImage(icone_pedra)

icone_papel = Image.open("Papel.png")
icone_papel = icone_papel.resize((50, 50), Image.LANCZOS)
icone_papel = ImageTk.PhotoImage(icone_papel)

icone_tesoura = Image.open("Tesoura.png")
icone_tesoura = icone_tesoura.resize((50, 50), Image.LANCZOS)
icone_tesoura = ImageTk.PhotoImage(icone_tesoura)

# BOTÃO PEDRA
btn_pedra = tk.Button(
    frame_baixo,
    command=lambda: jogar("pedra"),
    width=50,
    height=50,
    image=icone_pedra,
    bg=cor0,
    fg=cor0,
    compound="center",
    font=("Ivy 10 bold"),
    anchor="center",
    relief="flat"
)
btn_pedra.place(x=170, y=55)

# BOTÃO PAPEL
btn_papel = tk.Button(
    frame_baixo,
    command=lambda: jogar("papel"),
    width=50,
    height=50,
    image=icone_papel,
    bg=cor0,
    fg=cor0,
    compound="center",
    font=("Ivy 10 bold"),
    anchor="center",
    relief="flat"
)
btn_papel.place(x=40, y=50)

# BOTÃO TESOURA
btn_tesoura = tk.Button(
    frame_baixo,
    command=lambda: jogar("tesoura"),
    width=50,
    height=50,
    image=icone_tesoura,
    bg=cor0,
    fg=cor0,
    compound="center",
    font=("Ivy 10 bold"),
    anchor="center",
    relief="flat"
)
btn_tesoura.place(x=110, y=50)

# BOTÃO JOGAR / REINICIAR
btn_reiniciar = tk.Button(
    frame_baixo,
    text="Jogar",
    command=iniciar_jogo,
    width=30,
    height=1,
    bg=cor1,
    fg=cor0,
    compound="center",
    font=("Ivy 10 bold"),
    anchor="center",
    relief="flat"
)
btn_reiniciar.place(x=5, y=110)

# BOTÃO SAIR
btn_sair = tk.Button(
    frame_baixo,
    text="Sair",
    command=janela.destroy,
    width=30,
    height=1,
    bg=cor1,
    fg=cor0,
    compound="center",
    font=("Ivy 10 bold"),
    anchor="center",
    relief="flat"
)
btn_sair.place(x=5, y=140)

# INICIA O JOGO
iniciar_jogo()

janela.mainloop()