import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import ttk
from tkinter import messagebox


janela = Tk()
janela.title("Caixa Eletrônico")
janela.config(bg="#0A3352")         #COR DE FUNDO DA JANELA
janela.geometry("500x600")
janela.resizable(False, False)

#função para limpar tudo da janela
def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()

#função do menu principal
def menu():

    limpar_tela()

    tk.Label(
        janela,
        text="Menu Principal",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0A3352"
    ).pack(pady=40)

    tk.Label(
        janela,
        text="Escolha uma opção:",
        font=("Arial", 14),
        fg="white",
        bg="#0A3352"
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Consultar saldo",
        font=("Arial", 12, "bold"),
        bg="#1976D2",
        fg="white",
        width=20,
        height=2
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Depositar dinheiro",
        font=("Arial", 12, "bold"),
        bg="#1976D2",
        fg="white",
        width=20,
        height=2
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Sacar dinheiro",
        font=("Arial", 12, "bold"),
        bg="#1976D2",
        fg="white",
        width=20,
        height=2
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Sair",
        font=("Arial", 12, "bold"),
        bg="#D32F2F",
        fg="white",
        width=20,
        height=2
    ).pack(pady=10)


# titulo
tk.Label(
    janela,
    text="Bem-vindo ao Caixa Eletrônico!",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#0A3352"
).pack(pady=40)


# conta
tk.Label(
    janela,
    text="Digite sua conta:",
    font=("Arial", 12),
    fg="white",
    bg="#0A3352"
).pack()

entrada_conta = tk.Entry(
    janela,
    font=("Arial", 14),
    width=25,
    justify="center"
)

entrada_conta.pack(pady=10)

# senha
tk.Label(
    janela,
    text="Digite sua senha:",
    font=("Arial", 12),
    fg="white",
    bg="#0A3352"
).pack(pady=5)

entrada_senha = tk.Entry(
    janela,
    font=("Arial", 14),
    width=25,
    show="*",
    justify="center"
)

entrada_senha.pack(pady=10)


#função entrar
def entrar():

    conta = entrada_conta.get()
    senha = entrada_senha.get()

    if conta == "":
        messagebox.showerror(
            "Erro",
            "Digite sua conta."
        )

    elif senha == "":
        messagebox.showerror(
            "Erro",
            "Digite sua senha."
        )

    else:
        messagebox.showinfo(
            "Login",
            "Entrada realizada com sucesso!"
        )

        menu()                     #criar função menu, onde mostra "consultar saldo", "depositar dinheiro", "sacar dinheiro", e "sair"

#botão entrar
tk.Button(
    janela,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    width=20,
    height=2,
    command=entrar
).pack(pady=30)

janela.mainloop()