import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import ttk
from tkinter import messagebox

cores_canvas = {
    "Preto": "#000000",
    "Marrom": "#8B4513",
    "Vermelho": "#FF0000",
    "Laranja": "#FFA500",
    "Amarelo": "#FFFF00",
    "Verde": "#008000",
    "Azul": "#0000FF",
    "Violeta": "#800080",
    "Cinza": "#808080",
    "Branco": "#FFFFFF",
    "Dourado": "#FFD700",
    "Prata": "#C0C0C0"
}

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
janela.geometry("600x300")

def desenhar_resistor():
    cor1 = cores_canvas[primeira_cor.get()]
    cor2 = cores_canvas[segunda_cor.get()]
    cor3 = cores_canvas[terceira_cor.get()]
    cor4 = cores_canvas[quarta_cor.get()]

    # apaga o desenho anterior
    canvas.delete("all")

    # corpo do resistor
    canvas.create_rectangle(
        50, 40,
        350, 100,
        fill="light gray",
        outline="black"
    )

    # primeira faixa
    canvas.create_rectangle(
        120, 40,
        140, 100,
        fill=cor1
    )

    # segunda faixa
    canvas.create_rectangle(
        160, 40,
        180, 100,
        fill=cor2
    )

    # terceira faixa
    canvas.create_rectangle(
        200, 40,
        220, 100,
        fill=cor3
    )

    # faixa de tolerância
    canvas.create_rectangle(
        280, 40,
        300, 100,
        fill=cor4
    )

    canvas.create_line(
        0,
        75,
        50,
        75,
        width=5
    )

    canvas.create_line(
        350,
        75,
        400,
        75,
        width=5
    )

def calculo():

    try:
        if not all([
            primeira_cor.get(),
            segunda_cor.get(),
            terceira_cor.get(),
            quarta_cor.get()
        ]):
            raise ValueError("Selecione todas as quatro cores.")

        x = (
            (cores[primeira_cor.get()] * 10 + cores[segunda_cor.get()])
            * 10 ** cores[terceira_cor.get()]
        )

        y = (f'{tolerancias[quarta_cor.get()]}')

        desenhar_resistor()  # chama a função para desenhar o resistor com as cores selecionadas

        if x < 1_000:
                messagebox.showinfo(
                "Resultado",
                (f'{x}Ω ± {y}%')
            )
        elif x < 1_000_000:
                messagebox.showinfo(
                "Resultado",
                (f'{x/1000}KΩ ± {y}')
            )
        else:
            messagebox.showinfo(
                "Resultado",
                (f'{x/1000000}MΩ ± {y}%')
            )

    except ValueError:
        messagebox.showerror("Erro", "Selecione todas as quatro cores.")

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

# Área para desenhar o resistor
canvas = Canvas(
    janela,
    width=400,
    height=160,
    bg="white"
)

canvas.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=0,
    pady=0
)

resistor = canvas.create_rectangle(
    50,
    40,
    350,
    100,
    fill="light gray"
)

perna_resistor_esquerda = canvas.create_line(
    0,
    75,
    50,
    75,
    width=5
)

perna_resistor_direita = canvas.create_line(
    350,
    75,
    400,
    75,
    width=5
)

resultado = tk.Button(janela, text="Resultado:", bg='white', command=calculo)
resultado.grid(      
    row=4,
    column=0,
    pady=5
)

#===========================================================================
#segunda parte    800x300

# Parede/divisor vertical no meio da janela
parede = tk.Frame(
    janela,
    bg="black",
    width=3
)

parede.place(
    x=403,
    y=-100,
    relheight=1
)

parede_baixo = tk.Frame(
    janela,
    bg="black",
    width=3
)

parede_baixo.place(
    x=403,
    y=200,
    width=300,
    height=3
)

valor_ohms = tk.Entry(janela, width=20)
valor_ohms.grid(
    row=2,
    column=4,
    padx=15,
    pady=10
)

def resistor_por_valor():
        
        valor = float(valor_ohms.get())

        if valor <= 0:
            messagebox.showerror(
                "Erro",
                "Digite um valor maior que zero."
            )
            return

        # Descobre o expoente da potência de 10
        expoente = 0
        valor_normalizado = valor

        while valor_normalizado >= 100:
            valor_normalizado /= 10
            expoente += 1

        while valor_normalizado < 10:
            valor_normalizado *= 10
            expoente -= 1

        # Arredonda os dois primeiros algarismos
        numero = round(valor_normalizado)

        # Caso o arredondamento vire 100
        if numero == 100:
            numero = 10
            expoente += 1

        primeiro = numero // 10
        segundo = numero % 10

        # Verifica se pode ser representado por 4 faixas
        if primeiro > 9 or segundo > 9 or expoente < 0 or expoente > 9:
            messagebox.showerror(
                "Erro",
                "Esse valor não pode ser representado por um resistor de 4 faixas."
            )
            return

        # Converte os números para as cores
        numeros_para_cores = {
            0: "Preto",
            1: "Marrom",
            2: "Vermelho",
            3: "Laranja",
            4: "Amarelo",
            5: "Verde",
            6: "Azul",
            7: "Violeta",
            8: "Cinza",
            9: "Branco"
        }

        cor1 = numeros_para_cores[primeiro]
        cor2 = numeros_para_cores[segundo]
        cor3 = numeros_para_cores[expoente]

        # Coloca as cores nos Combobox
        primeira_cor.set(cor1)
        segunda_cor.set(cor2)
        terceira_cor.set(cor3)

        # Tolerância padrão
        quarta_cor.set("Dourado")

        # Desenha o resistor
        desenhar_resistor()

botao_ohms = tk.Button(
    janela,
    text="Calcular cores do resistor",
    command=resistor_por_valor
)

botao_ohms.grid(
    row=3,
    column=4,
    padx=15,
    pady=10
)

label_ohms = tk.Label(
    janela,
    text="Digite o valor do\n resistor em ohms (Ω):",
    font=("Arial", 11)
)
label_ohms.grid(
    row=1,
    column=4,
    padx=15,
    pady=0
)

janela.mainloop()