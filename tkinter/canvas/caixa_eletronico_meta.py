import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import ttk
from tkinter import messagebox


janela = Tk()
janela.title("Caixa Eletrônico")
janela.config(bg="#0A3352")
janela.geometry("500x600")
janela.resizable(False, False)

saldo = 1000
conta = ""

ARQUIVO_CONTAS = "contas_caixa.txt"


def carregar_contas():
    
    contas = {}

    try:
        with open(ARQUIVO_CONTAS, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if linha:
                    numero_conta, saldo_conta = linha.split(";")

                    contas[numero_conta] = float(saldo_conta)

    except FileNotFoundError:

        with open(ARQUIVO_CONTAS, "w", encoding="utf-8"):
            pass

    return contas

contas = carregar_contas()


# função para salvar contas em um arquivo.txt
def salvar_contas():
    
    with open(ARQUIVO_CONTAS, "w", encoding="utf-8") as arquivo:

        for numero_conta, saldo_conta in contas.items():

            arquivo.write(
                f"{numero_conta};{saldo_conta}\n"
            )


# função para limpar tudo da janela
def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()


# função do menu principal
def menu():

    limpar_tela()

    tk.Label(
        janela,
        text="CAIXA ELETRÔNICO",
        font=("Arial", 11, "bold"),
        fg="#64B5F6",
        bg="#0A3352"
    ).pack(pady=(25, 5))

    tk.Label(
        janela,
        text=f"Conta: {conta}",
        font=("Arial", 11, "bold"),
        fg="#B0BEC5",
        bg="#0A3352"
    ).pack(pady=5)

    tk.Label(
        janela,
        text="MENU PRINCIPAL",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="#0A3352"
    ).pack(pady=15)

    tk.Label(
        janela,
        text=f"Saldo disponível: R$ {saldo:.2f}",
        font=("Arial", 12, "bold"),
        fg="#66FF99",
        bg="#164B70",
        width=35,
        pady=10
    ).pack(pady=5)

    tk.Label(
        janela,
        text="Escolha uma opção",
        font=("Arial", 12),
        fg="#B0BEC5",
        bg="#0A3352"
    ).pack(pady=15)

    tk.Button(
        janela,
        text="💰  Consultar saldo",
        font=("Arial", 12, "bold"),
        bg="#1976D2",
        activebackground="#2196F3",
        activeforeground="white",
        command=consultar_saldo,
        fg="white",
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=6)

    tk.Button(
        janela,
        text="💵  Depositar dinheiro",
        font=("Arial", 12, "bold"),
        bg="#00897B",
        activebackground="#00A88F",
        activeforeground="white",
        fg="white",
        command=depositar_dinheiro,
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=6)

    tk.Button(
        janela,
        text="💸  Sacar dinheiro",
        font=("Arial", 12, "bold"),
        bg="#F57C00",
        activebackground="#FF9800",
        activeforeground="white",
        fg="white",
        command=sacar_dinheiro,
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=6)

    tk.Button(
        janela,
        text="🚪  Sair",
        font=("Arial", 12, "bold"),
        bg="#D32F2F",
        activebackground="#EF5350",
        activeforeground="white",
        fg="white",
        command=quit,
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=6)


# ========== FUNÇÕES PARA OS BOTÕES DO MENU ==========

def consultar_saldo():

    messagebox.showinfo(
        "Consultar saldo",
        f"Conta: {conta}\n\n"
        f"Seu saldo atual é:\n"
        f"R$ {saldo:.2f}"
    )


def depositar_dinheiro():

    limpar_tela()

    tk.Label(
        janela,
        text="CAIXA ELETRÔNICO",
        font=("Arial", 11, "bold"),
        fg="#64B5F6",
        bg="#0A3352"
    ).pack(pady=(25, 5))

    tk.Label(
        janela,
        text=f"Conta: {conta}",
        font=("Arial", 11, "bold"),
        fg="#B0BEC5",
        bg="#0A3352"
    ).pack(pady=5)

    tk.Label(
        janela,
        text="DEPÓSITO",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="#0A3352"
    ).pack(pady=20)

    tk.Label(
        janela,
        text="Digite quanto queira depositar:",
        font=("Arial", 13),
        fg="#B0BEC5",
        bg="#0A3352"
    ).pack(pady=10)

    valor = tk.Entry(
        janela,
        font=("Arial", 15),
        width=25,
        justify="center",
        bg="white",
        fg="#263238",
        relief="flat",
        bd=0
    )

    valor.pack(pady=10, ipady=7)

    tk.Label(
        janela,
        text="Cédulas disponíveis: R$ 2, 5, 10, 20, 50 e 100",
        font=("Arial", 9),
        fg="#90A4AE",
        bg="#0A3352"
    ).pack(pady=5)

    tk.Button(
        janela,
        text="💵  DEPOSITAR",
        font=("Arial", 12, "bold"),
        bg="#00897B",
        activebackground="#00A88F",
        activeforeground="white",
        fg="white",
        command=lambda: somar_deposito(valor),
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        janela,
        text="←  VOLTAR",
        font=("Arial", 11, "bold"),
        bg="#455A64",
        activebackground="#607D8B",
        activeforeground="white",
        fg="white",
        command=menu,
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)


def somar_deposito(valor):

    global saldo

    try:
        valor = float(valor.get())

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Digite um valor numérico válido."
        )

        return

    valor = int(valor)

    cedulas_deposito = [100, 50, 20, 10, 5, 2]
    restante = valor

    for cedula in cedulas_deposito:

        quantidade = restante // cedula
        restante %= cedula

    if restante != 0:

        messagebox.showerror(
            "Erro",
            "Digite um valor que possa ser convertido em cédulas."
        )

        return

    saldo += valor
    contas[conta] = saldo
    salvar_contas()

    messagebox.showinfo(
        "Depósito aplicado com sucesso!",
        f"Agora seu saldo é R$ {saldo:.2f}"
    )

    menu()


def sacar_dinheiro():

    limpar_tela()

    tk.Label(
        janela,
        text="CAIXA ELETRÔNICO",
        font=("Arial", 11, "bold"),
        fg="#64B5F6",
        bg="#0A3352"
    ).pack(pady=(25, 5))

    tk.Label(
        janela,
        text=f"Conta: {conta}",
        font=("Arial", 11, "bold"),
        fg="#B0BEC5",
        bg="#0A3352"
    ).pack(pady=5)

    tk.Label(
        janela,
        text="SAQUE",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="#0A3352"
    ).pack(pady=20)

    tk.Label(
        janela,
        text="Digite quanto queira sacar:",
        font=("Arial", 13),
        fg="#B0BEC5",
        bg="#0A3352"
    ).pack(pady=10)

    valor = tk.Entry(
        janela,
        font=("Arial", 15),
        width=25,
        justify="center",
        bg="white",
        fg="#263238",
        relief="flat",
        bd=0
    )

    valor.pack(pady=10, ipady=7)

    tk.Label(
        janela,
        text="Cédulas disponíveis: R$ 2, 5, 10, 20, 50 e 100",
        font=("Arial", 9),
        fg="#90A4AE",
        bg="#0A3352"
    ).pack(pady=5)

    tk.Button(
        janela,
        text="💸  SACAR",
        font=("Arial", 12, "bold"),
        bg="#F57C00",
        activebackground="#FF9800",
        activeforeground="white",
        fg="white",
        command=lambda: retirar_do_deposito(valor),
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        janela,
        text="←  VOLTAR",
        font=("Arial", 11, "bold"),
        bg="#455A64",
        activebackground="#607D8B",
        activeforeground="white",
        fg="white",
        command=menu,
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)


def retirar_do_deposito(valor):

    global saldo

    try:
        valor = float(valor.get())

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Digite um valor numérico válido."
        )

        return

    # Verifica se o valor é positivo
    if valor <= 0:

        messagebox.showerror(
            "Erro",
            "Digite um valor maior que zero."
        )

        return

    # Verifica se possui saldo suficiente
    if valor > saldo:

        messagebox.showerror(
            "Erro",
            "Saldo insuficiente."
        )

        return

    # Converte para inteiro, pois estamos trabalhando com cédulas
    valor = int(valor)

    cedulas = [100, 50, 20, 10, 5, 2]
    cedulas_entregues = {}

    restante = valor

    # Calcula as cédulas necessárias
    for cedula in cedulas:

        quantidade = restante // cedula

        if quantidade > 0:

            cedulas_entregues[cedula] = quantidade
            restante %= cedula

    # Caso não seja possível formar o valor
    if restante != 0:

        messagebox.showerror(
            "Erro",
            "Não é possível formar esse valor com as cédulas disponíveis."
        )

        return

    # Retira o dinheiro do saldo
    saldo -= valor
    contas[conta] = saldo
    salvar_contas()

    # Monta a mensagem das cédulas
    mensagem = "Saque realizado com sucesso!\n\n"
    mensagem += "Cédulas entregues:\n"

    for cedula, quantidade in cedulas_entregues.items():

        mensagem += f"{quantidade}x R$ {cedula},00\n"

    mensagem += f"\nValor sacado: R$ {valor:.2f}"
    mensagem += f"\nSaldo restante: R$ {saldo:.2f}"

    messagebox.showinfo(
        "Saque",
        mensagem
    )

    menu()


# =========================================================
# TELA INICIAL
# =========================================================

tk.Label(
    janela,
    text="CAIXA ELETRÔNICO",
    font=("Arial", 12, "bold"),
    fg="#64B5F6",
    bg="#0A3352"
).pack(pady=(35, 5))


tk.Label(
    janela,
    text="Bem-vindo!",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#0A3352"
).pack(pady=5)


tk.Label(
    janela,
    text="Digite seus dados para acessar sua conta",
    font=("Arial", 10),
    fg="#B0BEC5",
    bg="#0A3352"
).pack(pady=(0, 25))


# conta

tk.Label(
    janela,
    text="NÚMERO DA CONTA",
    font=("Arial", 10, "bold"),
    fg="#64B5F6",
    bg="#0A3352"
).pack()


entrada_conta = tk.Entry(
    janela,
    font=("Arial", 14),
    width=25,
    justify="center",
    bg="white",
    fg="#263238",
    relief="flat",
    bd=0
)

entrada_conta.pack(pady=10, ipady=7)


# senha

tk.Label(
    janela,
    text="SENHA",
    font=("Arial", 10, "bold"),
    fg="#64B5F6",
    bg="#0A3352"
).pack(pady=5)


entrada_senha = tk.Entry(
    janela,
    font=("Arial", 14),
    width=25,
    show="*",
    justify="center",
    bg="white",
    fg="#263238",
    relief="flat",
    bd=0
)

entrada_senha.pack(pady=10, ipady=7)


# função entrar

def entrar():

    global conta, saldo

    conta_digitada = entrada_conta.get()
    senha = entrada_senha.get()

    if conta_digitada == "":

        messagebox.showerror(
            "Erro",
            "Digite sua conta."
        )

        return

    elif senha == "":

        messagebox.showerror(
            "Erro",
            "Digite sua senha."
        )

        return

    elif conta_digitada not in contas:

        messagebox.showerror(
            "Erro",
            "Conta não encontrada."
        )

        return

    else:

        conta = conta_digitada
        saldo = contas[conta]

        messagebox.showinfo(
            "Login",
            "Entrada realizada com sucesso!"
        )

        menu()


# botão entrar

tk.Button(
    janela,
    text="🔐  ENTRAR",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    activebackground="#2196F3",
    activeforeground="white",
    fg="white",
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=entrar
).pack(pady=25)


janela.mainloop()
