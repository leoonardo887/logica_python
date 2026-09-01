import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import ttk
from tkinter import messagebox

cores = {
    "Preto": 0,
    "Marrom": 1,
    "Vermelho": 2,
    "Laranja": 3,
    "Amarelo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Cinza": 8,
    "Branco": 9
}

tolerancias = {
    "Marrom": 1,      # ±1%
    "Vermelho": 2,   # ±2%
    "Verde": 0.5,     # ±0,5%
    "Azul": 0.25,    # ±0,25%
    "Violeta": 0.1,  # ±0,1%
    "Cinza": 0.05,   # ±0,05%
    "Dourado": 5,    # ±5%
    "Prata": 10      # ±10%
}

janela = Tk()
janela.geometry("400x300")


# Cores
cor0 = "#000000"  # Preto
cor1 = "#8B4513"  # Marrom
cor2 = "#FF0000"  # Vermelho
cor3 = "#FFA500"  # Laranja
cor4 = "#FFFF00"  # Amarelo
cor5 = "#008000"  # Verde
cor6 = "#0000FF"  # Azul
cor7 = "#800080"  # Violeta
cor8 = "#808080"  # Cinza
cor9 = "#FFFFFF"  # Branco

cor_dourado = "#FFD700"
cor_prateado = "#C0C0C0"


# Combobox da primeira cor
primeira_cor = ttk.Combobox(
    janela,
    values=list(cores.keys())
)

primeira_cor.grid(
    row=0,
    column=0,
    padx=0,
    pady=0
)
#combobox da segunda cor
segunda_cor = ttk.Combobox(
    janela,
    values=list(cores.keys())
)

segunda_cor.grid(
    row=1,
    column=0,
    padx=0,
    pady=10
)

terceira_cor = ttk.Combobox(
    janela,
    values=list(cores.keys())
)

terceira_cor.grid(
    row=2,
    column=0,
    padx=0,
    pady=4
)

quarta_cor = ttk.Combobox(
    janela,
    values=list(tolerancias.keys())
)

quarta_cor.grid(
    row=3,
    column=0,
    pady=10
)
#labels de mensagem
label_1 = tk.Label(janela, text="Selecione a primeira cor do resistor. ", font=("Arial", 11))
label_1.grid(
    row=0,
    column=1,
    )

label_2 = tk.Label(janela, text="Selecione a segunda cor do resistor. ", font=("Arial", 11))
label_2.grid(
    row=1,
    column=1,
    pady=10
    )

label_3 = tk.Label(janela, text="Selecione a terceira cor do resistor. ", font=("Arial", 11))
label_3.grid(
    row=2,
    column=1,
    pady=4
    )

label_4 = tk.Label(janela, text="Selecione a faixa de tolerância do\n resistor. ", font=("Arial", 11))
label_4.grid(
    row=3,
    column=1,
    pady=4
    )

# Área para desenhar o resistor futuramente
canvas = Canvas(
    janela,
    width=400,
    height=160,
    bg="light blue"
)

canvas.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=0,
    pady=0
)

def calculo():
    x = (
        (cores[primeira_cor.get()] * 10 + cores[segunda_cor.get()])
        * 10 ** cores[terceira_cor.get()]
    )
    messagebox.showinfo(
        "Resultado",
        (f'{x}Ω')
    )
    print(x)

resultado = tk.Button(janela, text="Resultado:", command=calculo)
resultado.grid(
    row=4,
    column=0,
    pady=0
)

janela.mainloop()