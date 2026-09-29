import tkinter as tk
from tkinter import messagebox
import os


# ============================================================
# CONFIGURAÇÕES
# ============================================================

SALDO_INICIAL = 1000
ARQUIVO_SALDOS = "saldos.txt"

# Cédulas disponíveis no caixa
CEDULAS = [100, 50, 20, 10, 5, 2]


# ============================================================
# FUNÇÕES DE ARQUIVO
# ============================================================

def carregar_saldo(conta):
    """
    Procura a conta no arquivo.
    Se encontrar, retorna o saldo salvo.
    Se não encontrar, retorna R$ 1.000,00.
    """

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

    # Conta ainda não utilizada
    return SALDO_INICIAL


def salvar_saldo(conta, saldo):
    """
    Salva o saldo da conta no arquivo.
    Se a conta já existir, atualiza o saldo.
    """

    contas = {}

    # Lê as contas existentes
    if os.path.exists(ARQUIVO_SALDOS):

        arquivo = open(ARQUIVO_SALDOS, "r", encoding="utf-8")

        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) == 2:
                contas[dados[0]] = dados[1]

        arquivo.close()

    # Atualiza ou adiciona a conta
    contas[conta] = str(saldo)

    # Reescreve o arquivo
    arquivo = open(ARQUIVO_SALDOS, "w", encoding="utf-8")

    for conta_salva in contas:
        arquivo.write(
            conta_salva + ";" + contas[conta_salva] + "\n"
        )

    arquivo.close()


# ============================================================
# CLASSE PRINCIPAL
# ============================================================

class CaixaEletronico:

    def __init__(self, janela):

        self.janela = janela

        self.janela.title("Caixa Eletrônico")
        self.janela.geometry("500x600")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#17202A")

        # Variáveis do sistema
        self.conta = ""
        self.senha = ""
        self.saldo = SALDO_INICIAL

        # Contadores de cédulas
        self.qtd_100 = 0
        self.qtd_50 = 0
        self.qtd_20 = 0
        self.qtd_10 = 0
        self.qtd_5 = 0
        self.qtd_2 = 0

        # Mostra a primeira tela
        self.tela_login()


    # ========================================================
    # FUNÇÕES DE INTERFACE
    # ========================================================

    def limpar_tela(self):

        for widget in self.janela.winfo_children():
            widget.destroy()


    def titulo(self, texto):

        tk.Label(
            self.janela,
            text=texto,
            font=("Arial", 24, "bold"),
            bg="#17202A",
            fg="white"
        ).pack(pady=30)


    def botao(self, texto, comando, cor="#2874A6"):

        tk.Button(
            self.janela,
            text=texto,
            command=comando,
            font=("Arial", 13, "bold"),
            bg=cor,
            fg="white",
            width=25,
            height=2
        ).pack(pady=6)


    # ========================================================
    # TELA DE CONTA E SENHA
    # ========================================================

    def tela_login(self):

        self.limpar_tela()

        self.titulo("CAIXA ELETRÔNICO")

        tk.Label(
            self.janela,
            text="Digite sua conta:",
            font=("Arial", 13),
            bg="#17202A",
            fg="white"
        ).pack(pady=5)

        self.entrada_conta = tk.Entry(
            self.janela,
            font=("Arial", 16),
            justify="center"
        )
        self.entrada_conta.pack(pady=5)

        tk.Label(
            self.janela,
            text="Digite sua senha:",
            font=("Arial", 13),
            bg="#17202A",
            fg="white"
        ).pack(pady=5)

        self.entrada_senha = tk.Entry(
            self.janela,
            show="*",
            font=("Arial", 16),
            justify="center"
        )
        self.entrada_senha.pack(pady=5)

        self.botao(
            "ENTRAR",
            self.entrar,
            "#1E8449"
        )


    def entrar(self):

        self.conta = self.entrada_conta.get().strip()
        self.senha = self.entrada_senha.get().strip()

        if self.conta == "":
            messagebox.showerror(
                "Erro",
                "Digite sua conta."
            )
            return

        if self.senha == "":
            messagebox.showerror(
                "Erro",
                "Digite sua senha."
            )
            return

        # Carrega o saldo salvo para essa conta
        self.saldo = carregar_saldo(self.conta)

        self.menu()


    # ========================================================
    # MENU PRINCIPAL
    # ========================================================

    def menu(self):

        self.limpar_tela()

        self.titulo("MENU PRINCIPAL")

        tk.Label(
            self.janela,
            text=f"Conta: {self.conta}",
            font=("Arial", 11),
            bg="#17202A",
            fg="#AAB7B8"
        ).pack(pady=5)

        self.botao(
            "1 - Consultar saldo",
            self.consultar_saldo
        )

        self.botao(
            "2 - Sacar dinheiro",
            self.tela_saque
        )

        self.botao(
            "3 - Depositar dinheiro",
            self.tela_deposito
        )

        self.botao(
            "4 - Sair",
            self.sair,
            "#922B21"
        )


    # ========================================================
    # CONSULTAR SALDO
    # ========================================================

    def consultar_saldo(self):

        mensagem = (
            "Seu saldo atual é:\n\n"
            f"R$ {self.saldo:.2f}".replace(".", ",")
        )

        messagebox.showinfo(
            "Consulta de saldo",
            mensagem
        )


    # ========================================================
    # TELA DE SAQUE
    # ========================================================

    def tela_saque(self):

        self.limpar_tela()

        self.titulo("SAQUE")

        tk.Label(
            self.janela,
            text="Digite o valor para saque:",
            font=("Arial", 14),
            bg="#17202A",
            fg="white"
        ).pack(pady=10)

        self.entrada_valor = tk.Entry(
            self.janela,
            font=("Arial", 18),
            justify="center"
        )
        self.entrada_valor.pack(pady=10)

        self.botao(
            "CONFIRMAR SAQUE",
            self.realizar_saque,
            "#1E8449"
        )

        self.botao(
            "VOLTAR",
            self.menu,
            "#566573"
        )


    # ========================================================
    # REALIZAR SAQUE
    # ========================================================

    def realizar_saque(self):

        valor_texto = self.entrada_valor.get().strip()

        # Verifica se foi digitado alguma coisa
        if valor_texto == "":
            messagebox.showerror(
                "Erro",
                "Digite um valor."
            )
            return

        # Impede valores fracionários
        if "," in valor_texto or "." in valor_texto:
            messagebox.showerror(
                "Erro",
                "Valores fracionários não são aceitos.\n"
                "Digite um valor inteiro."
            )
            return

        # Verifica se o valor contém apenas números
        if not valor_texto.isdigit():

            messagebox.showerror(
                "Erro",
                "Digite apenas números."
            )
            return

        valor = int(valor_texto)

        # Impede zero e valores negativos
        if valor <= 0:

            messagebox.showerror(
                "Erro",
                "O valor do saque deve ser maior que zero."
            )
            return

        # Verifica saldo
        if valor > self.saldo:

            messagebox.showerror(
                "Saldo insuficiente",
                "Você não possui saldo suficiente para realizar este saque."
            )
            return

        # Verifica se o caixa consegue formar o valor
        if not self.valor_pode_ser_sacado(valor):

            messagebox.showerror(
                "Valor inválido",
                "O caixa não possui cédulas suficientes para "
                "formar esse valor.\n\n"
                "Cédulas disponíveis:\n"
                "R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2"
            )
            return

        # Calcula as cédulas
        cedulas = self.calcular_cedulas(valor)

        # Atualiza o saldo
        self.saldo -= valor

        # Monta a mensagem
        mensagem = "Saque realizado com sucesso!\n\n"
        mensagem += "Entregar:\n"

        for cedula in cedulas:

            quantidade = cedulas[cedula]

            if quantidade > 0:

                mensagem += (
                    f"{quantidade} cédula(s) de R$ {cedula}\n"
                )

        mensagem += (
            f"\nSaldo atual: R$ {self.saldo:.2f}"
            .replace(".", ",")
        )

        messagebox.showinfo(
            "Saque realizado",
            mensagem
        )

        self.menu()


    # ========================================================
    # VERIFICA SE O VALOR PODE SER FORMADO
    # ========================================================

    def valor_pode_ser_sacado(self, valor):

        restante = valor

        for cedula in CEDULAS:

            quantidade = restante // cedula

            restante = restante % cedula

        # Se sobrar alguma coisa, não é possível formar o valor
        if restante == 0:
            return True
        else:
            return False


    # ========================================================
    # CALCULA A QUANTIDADE DE CÉDULAS
    # ========================================================

    def calcular_cedulas(self, valor):

        cedulas = {}

        restante = valor

        # Laço de repetição para calcular as cédulas
        for cedula in CEDULAS:

            quantidade = restante // cedula

            cedulas[cedula] = quantidade

            restante = restante % cedula

        return cedulas


    # ========================================================
    # TELA DE DEPÓSITO
    # ========================================================

    def tela_deposito(self):

        self.limpar_tela()

        self.titulo("DEPÓSITO")

        tk.Label(
            self.janela,
            text="Digite o valor para depósito:",
            font=("Arial", 14),
            bg="#17202A",
            fg="white"
        ).pack(pady=10)

        self.entrada_valor = tk.Entry(
            self.janela,
            font=("Arial", 18),
            justify="center"
        )
        self.entrada_valor.pack(pady=10)

        self.botao(
            "CONFIRMAR DEPÓSITO",
            self.realizar_deposito,
            "#1E8449"
        )

        self.botao(
            "VOLTAR",
            self.menu,
            "#566573"
        )


    # ========================================================
    # REALIZAR DEPÓSITO
    # ========================================================

    def realizar_deposito(self):

        valor_texto = self.entrada_valor.get().strip()

        if valor_texto == "":

            messagebox.showerror(
                "Erro",
                "Digite um valor."
            )
            return

        # Impede valores fracionários
        if "," in valor_texto or "." in valor_texto:

            messagebox.showerror(
                "Erro",
                "Valores fracionários não são aceitos.\n"
                "Digite um valor inteiro."
            )
            return

        # Verifica se são números
        if not valor_texto.isdigit():

            messagebox.showerror(
                "Erro",
                "Digite apenas números."
            )
            return

        valor = int(valor_texto)

        # Impede zero ou valores negativos
        if valor <= 0:

            messagebox.showerror(
                "Erro",
                "O valor do depósito deve ser maior que zero."
            )
            return

        # Atualiza o saldo
        self.saldo += valor

        messagebox.showinfo(
            "Depósito realizado",
            "Depósito realizado com sucesso!\n\n"
            f"Valor: R$ {valor},00\n"
            f"Saldo atual: R$ {self.saldo:.2f}".replace(".", ",")
        )

        self.menu()


    # ========================================================
    # SAIR
    # ========================================================

    def sair(self):

        resposta = messagebox.askyesno(
            "Sair",
            "Deseja realmente sair?\n\n"
            "O saldo será salvo."
        )

        if resposta:

            # Salva o saldo antes de fechar
            salvar_saldo(
                self.conta,
                self.saldo
            )

            messagebox.showinfo(
                "Caixa Eletrônico",
                "Obrigado por usar nosso sistema!"
            )

            # Volta para a tela de conta e senha
            self.tela_login()


# ============================================================
# INICIAR PROGRAMA
# ============================================================

janela = tk.Tk()

caixa = CaixaEletronico(janela)

janela.mainloop()