import tkinter as tk
from tkinter import messagebox
import os


# ============================================================
# CONFIGURAÇÕES
# ============================================================

SALDO_INICIAL = 1000
ARQUIVO_SALDOS = "saldos.txt"

CEDULAS = [100, 50, 20, 10, 5, 2]


# ============================================================
# VARIÁVEIS DO SISTEMA
# ============================================================

conta = ""
senha = ""
saldo = SALDO_INICIAL

janela = tk.Tk()

# ============================================================
# FUNÇÕES DE ARQUIVO
# ============================================================

def carregar_saldo(conta):

    if not os.path.exists(ARQUIVO_SALDOS):
        return SALDO_INICIAL

    arquivo = open(ARQUIVO_SALDOS, "r", encoding="utf-8")

    for linha in arquivo:

        dados = linha.strip().split(";")

        if len(dados) == 2:

            conta_salva = dados[0]
            saldo_salvo = dados[1]

            if conta_salva == conta:

                arquivo.close()
                return float(saldo_salvo)

    arquivo.close()

    return SALDO_INICIAL


def salvar_saldo(conta, saldo):

    contas = {}

    if os.path.exists(ARQUIVO_SALDOS):

        arquivo = open(
            ARQUIVO_SALDOS,
            "r",
            encoding="utf-8"
        )

        for linha in arquivo:

            dados = linha.strip().split(";")

            if len(dados) == 2:

                contas[dados[0]] = dados[1]

        arquivo.close()

    contas[conta] = str(saldo)

    arquivo = open(
        ARQUIVO_SALDOS,
        "w",
        encoding="utf-8"
    )

    for conta_salva in contas:

        arquivo.write(
            conta_salva
            + ";"
            + contas[conta_salva]
            + "\n"
        )

    arquivo.close()


# ============================================================
# FUNÇÕES DE INTERFACE
# ============================================================

def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()


def titulo(texto):

    tk.Label(
        janela,
        text=texto,
        font=("Arial", 24, "bold"),
        bg="#17202A",
        fg="white"
    ).pack(pady=30)


def botao(texto, comando, cor="#2874A6"):

    tk.Button(
        janela,
        text=texto,
        command=comando,
        font=("Arial", 13, "bold"),
        bg=cor,
        fg="white",
        width=25,
        height=2
    ).pack(pady=6)


# ============================================================
# TELA DE LOGIN
# ============================================================

def tela_login():

    limpar_tela()

    titulo("CAIXA ELETRÔNICO")

    tk.Label(
        janela,
        text="Digite sua conta:",
        font=("Arial", 13),
        bg="#17202A",
        fg="white"
    ).pack(pady=5)

    global entrada_conta

    entrada_conta = tk.Entry(
        janela,
        font=("Arial", 16),
        justify="center"
    )

    entrada_conta.pack(pady=5)

    tk.Label(
        janela,
        text="Digite sua senha:",
        font=("Arial", 13),
        bg="#17202A",
        fg="white"
    ).pack(pady=5)

    global entrada_senha

    entrada_senha = tk.Entry(
        janela,
        show="*",
        font=("Arial", 16),
        justify="center"
    )

    entrada_senha.pack(pady=5)

    botao(
        "ENTRAR",
        entrar,
        "#1E8449"
    )


# ============================================================
# ENTRAR
# ============================================================

def entrar():

    global conta
    global senha
    global saldo

    conta = entrada_conta.get().strip()
    senha = entrada_senha.get().strip()

    if conta == "":

        messagebox.showerror(
            "Erro",
            "Digite sua conta."
        )

        return

    if senha == "":

        messagebox.showerror(
            "Erro",
            "Digite sua senha."
        )

        return

    saldo = carregar_saldo(conta)

    menu()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu():

    limpar_tela()

    titulo("MENU PRINCIPAL")

    tk.Label(
        janela,
        text=f"Conta: {conta}",
        font=("Arial", 11),
        bg="#17202A",
        fg="#AAB7B8"
    ).pack(pady=5)

    botao(
        "1 - Consultar saldo",
        consultar_saldo
    )

    botao(
        "2 - Sacar dinheiro",
        tela_saque
    )

    botao(
        "3 - Depositar dinheiro",
        tela_deposito
    )

    botao(
        "4 - Sair",
        sair,
        "#922B21"
    )


# ============================================================
# CONSULTAR SALDO
# ============================================================

def consultar_saldo():

    mensagem = (
        "Seu saldo atual é:\n\n"
        f"R$ {saldo:.2f}".replace(".", ",")
    )

    messagebox.showinfo(
        "Consulta de saldo",
        mensagem
    )


# ============================================================
# TELA DE SAQUE
# ============================================================

def tela_saque():

    limpar_tela()

    titulo("SAQUE")

    tk.Label(
        janela,
        text="Digite o valor para saque:",
        font=("Arial", 14),
        bg="#17202A",
        fg="white"
    ).pack(pady=10)

    global entrada_valor

    entrada_valor = tk.Entry(
        janela,
        font=("Arial", 18),
        justify="center"
    )

    entrada_valor.pack(pady=10)

    botao(
        "CONFIRMAR SAQUE",
        realizar_saque,
        "#1E8449"
    )

    botao(
        "VOLTAR",
        menu,
        "#566573"
    )


# ============================================================
# REALIZAR SAQUE
# ============================================================

def realizar_saque():

    global saldo

    valor_texto = entrada_valor.get().strip()

    if valor_texto == "":

        messagebox.showerror(
            "Erro",
            "Digite um valor."
        )

        return

    if "," in valor_texto or "." in valor_texto:

        messagebox.showerror(
            "Erro",
            "Valores fracionários não são aceitos.\n"
            "Digite um valor inteiro."
        )

        return

    if not valor_texto.isdigit():

        messagebox.showerror(
            "Erro",
            "Digite apenas números."
        )

        return

    valor = int(valor_texto)

    if valor <= 0:

        messagebox.showerror(
            "Erro",
            "O valor do saque deve ser maior que zero."
        )

        return

    if valor > saldo:

        messagebox.showerror(
            "Saldo insuficiente",
            "Você não possui saldo suficiente."
        )

        return

    if not valor_pode_ser_sacado(valor):

        messagebox.showerror(
            "Valor inválido",
            "O caixa não possui cédulas suficientes "
            "para formar esse valor.\n\n"
            "Cédulas disponíveis:\n"
            "R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2"
        )

        return

    cedulas = calcular_cedulas(valor)

    saldo -= valor

    mensagem = "Saque realizado com sucesso!\n\n"
    mensagem += "Entregar:\n"

    for cedula in cedulas:

        quantidade = cedulas[cedula]

        if quantidade > 0:

            mensagem += (
                f"{quantidade} cédula(s) de R$ {cedula}\n"
            )

    mensagem += (
        f"\nSaldo atual: R$ {saldo:.2f}"
        .replace(".", ",")
    )

    messagebox.showinfo(
        "Saque realizado",
        mensagem
    )

    menu()


# ============================================================
# VERIFICAR SE O VALOR PODE SER SACADO
# ============================================================

def valor_pode_ser_sacado(valor):

    restante = valor

    for cedula in CEDULAS:

        quantidade = restante // cedula

        restante = restante % cedula

    return restante == 0


# ============================================================
# CALCULAR CÉDULAS
# ============================================================

def calcular_cedulas(valor):

    cedulas = {}

    restante = valor

    for cedula in CEDULAS:

        quantidade = restante // cedula

        cedulas[cedula] = quantidade

        restante = restante % cedula

    return cedulas


# ============================================================
# TELA DE DEPÓSITO
# ============================================================

def tela_deposito():

    limpar_tela()

    titulo("DEPÓSITO")

    tk.Label(
        janela,
        text="Digite o valor para depósito:",
        font=("Arial", 14),
        bg="#17202A",
        fg="white"
    ).pack(pady=10)

    global entrada_valor

    entrada_valor = tk.Entry(
        janela,
        font=("Arial", 18),
        justify="center"
    )

    entrada_valor.pack(pady=10)

    botao(
        "CONFIRMAR DEPÓSITO",
        realizar_deposito,
        "#1E8449"
    )

    botao(
        "VOLTAR",
        menu,
        "#566573"
    )


# ============================================================
# REALIZAR DEPÓSITO
# ============================================================

def realizar_deposito():

    global saldo

    valor_texto = entrada_valor.get().strip()

    if valor_texto == "":

        messagebox.showerror(
            "Erro",
            "Digite um valor."
        )

        return

    if "," in valor_texto or "." in valor_texto:

        messagebox.showerror(
            "Erro",
            "Valores fracionários não são aceitos.\n"
            "Digite um valor inteiro."
        )

        return

    if not valor_texto.isdigit():

        messagebox.showerror(
            "Erro",
            "Digite apenas números."
        )

        return

    valor = int(valor_texto)

    if valor <= 0:

        messagebox.showerror(
            "Erro",
            "O valor do depósito deve ser maior que zero."
        )

        return

    saldo += valor

    messagebox.showinfo(
        "Depósito realizado",
        "Depósito realizado com sucesso!\n\n"
        f"Valor: R$ {valor},00\n"
        f"Saldo atual: R$ {saldo:.2f}".replace(".", ",")
    )

    menu()


# ============================================================
# SAIR
# ============================================================

def sair():

    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente sair?\n\n"
        "O saldo será salvo."
    )

    if resposta:

        salvar_saldo(
            conta,
            saldo
        )

        messagebox.showinfo(
            "Caixa Eletrônico",
            "Obrigado por usar nosso sistema!"
        )

        tela_login()


# ============================================================
# INICIAR PROGRAMA
# ============================================================

janela.title("Caixa Eletrônico")
janela.geometry("500x600")
janela.resizable(False, False)
janela.configure(bg="#17202A")

tela_login()

janela.mainloop()
