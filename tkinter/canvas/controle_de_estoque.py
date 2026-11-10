import tkinter as tk
from tkinter import messagebox
import json

janela = tk.Tk()
janela.title("Controle de Estoque")
janela.geometry("600x500")
janela.resizable(False, False)


# ARQUIVO DOS PRODUTOS
ARQUIVO_PRODUTOS = "produtos_de_estoque.json"


def carregar_produtos():
    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        produtos = []

        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, indent=4)

        return produtos

    except json.JSONDecodeError:
        messagebox.showerror(
            "Erro",
            "O arquivo produtos.json está com dados inválidos."
        )
        return []


def salvar_produtos(produtos):
    try:
        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
            json.dump(
                produtos,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar os produtos.\n{erro}"
        )


# Lista que guarda os produtos
produtos = carregar_produtos()


# CADASTRAR PRODUTO

def cadastrar_produto():

    # Pegando os valores digitados
    codigo_texto = entrada_codigo.get().strip()
    nome = entrada_nome.get().strip()
    quantidade_texto = entrada_quantidade.get().strip()
    minimo_texto = entrada_minimo.get().strip()
    preco_texto = entrada_preco.get().strip()

    # Verifica se algum campo está vazio
    if (
        codigo_texto == ""
        or nome == ""
        or quantidade_texto == ""
        or minimo_texto == ""
        or preco_texto == ""
    ):
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    # Converte os valores numéricos
    try:
        codigo = int(codigo_texto)
        quantidade = int(quantidade_texto)
        estoque_minimo = int(minimo_texto)
        preco = float(preco_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Código, quantidade e estoque mínimo devem ser inteiros.\n"
            "O preço deve ser um número."
        )
        return

    # Quantidade não pode ser negativa
    if quantidade < 0:
        messagebox.showerror(
            "Erro",
            "A quantidade não pode ser negativa."
        )
        return

    # Estoque mínimo não pode ser negativo
    if estoque_minimo < 0:
        messagebox.showerror(
            "Erro",
            "O estoque mínimo não pode ser negativo."
        )
        return

    # Preço precisa ser maior que zero
    if preco <= 0:
        messagebox.showerror(
            "Erro",
            "O preço deve ser maior que zero."
        )
        return

    # Verifica se o código já existe
    for produto in produtos:
        if produto["codigo"] == codigo:
            messagebox.showerror(
                "Erro",
                "Já existe um produto com esse código."
            )
            return

    # Cria o novo produto
    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "estoque_minimo": estoque_minimo,
        "preco": preco
    }

    # Adiciona o produto na lista
    produtos.append(novo_produto)

    # Salva no JSON
    salvar_produtos(produtos)

    # Mensagem de sucesso
    messagebox.showinfo(
        "Sucesso",
        "Produto cadastrado com sucesso!"
    )

    # Limpa os campos
    entrada_codigo.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_minimo.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)


# TÍTULO
titulo = tk.Label(
    janela,
    text="Cadastro de Produto",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)


# CAMPOS

frame = tk.Frame(janela)
frame.pack(pady=10)


tk.Label(
    frame,
    text="Código:"
).grid(row=0, column=0, padx=10, pady=8, sticky="e")

entrada_codigo = tk.Entry(frame)
entrada_codigo.grid(row=0, column=1)


tk.Label(
    frame,
    text="Nome:"
).grid(row=1, column=0, padx=10, pady=8, sticky="e")

entrada_nome = tk.Entry(frame)
entrada_nome.grid(row=1, column=1)


tk.Label(
    frame,
    text="Quantidade:"
).grid(row=2, column=0, padx=10, pady=8, sticky="e")

entrada_quantidade = tk.Entry(frame)
entrada_quantidade.grid(row=2, column=1)


tk.Label(
    frame,
    text="Estoque mínimo:"
).grid(row=3, column=0, padx=10, pady=8, sticky="e")

entrada_minimo = tk.Entry(frame)
entrada_minimo.grid(row=3, column=1)


tk.Label(
    frame,
    text="Preço unitário:"
).grid(row=4, column=0, padx=10, pady=8, sticky="e")

entrada_preco = tk.Entry(frame)
entrada_preco.grid(row=4, column=1)


# BOTÃO CADASTRAR
botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar Produto",
    font=("Arial", 12, "bold"),
    command=cadastrar_produto
)

botao_cadastrar.pack(pady=25)


janela.mainloop()