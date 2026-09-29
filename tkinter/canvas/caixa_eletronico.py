import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import ttk
from tkinter import messagebox


janela = Tk()
janela.title("Caixa Eletrônico")
janela.geometry("500x600")
janela.resizable(False, False)

# Cor de fundo da janela
janela.configure(bg="white")


#função para limpar tudo da janela
def limpar_tela():

    for widget in janela.winfo_children():
        widget.destroy()

# titúlo
tk.Label(
    janela,
    text="Bem-vindo ao Caixa Eletrônico!",
    font=("Arial", 20, "bold"),
    fg="black",
    bg="white"
).pack(pady=40)


# conta
tk.Label(
    janela,
    text="Digite sua conta:",
    font=("Arial", 12),
    fg="black",
    bg="white"
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
    fg="black",
    bg="white"
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
        limpar_tela()
        #menu()                     #criar função menu, onde mostra "consultar saldo", "depositar dinheiro", "sacar dinheiro", e "sair"

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