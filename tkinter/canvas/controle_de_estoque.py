import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from datetime import datetime


janela = tk.Tk()
janela.title("Controle de Estoque")
janela.geometry("850x950")
janela.resizable(False, False)


ARQUIVO_PRODUTOS = "produtos_de_estoque.json"
ARQUIVO_MOVIMENTACOES = "movimentacoes_estoque.json"


def carregar_dados(arquivo):

    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo_json:
            dados = json.load(arquivo_json)

            if not isinstance(dados, list):
                raise ValueError("O conteúdo deve ser uma lista.")

            return dados

    except FileNotFoundError:

        try:
            with open(arquivo, "w", encoding="utf-8") as arquivo_json:
                json.dump([], arquivo_json, indent=4)

            return []

        except OSError as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível criar o arquivo.\n{erro}"
            )
            return []

    except (json.JSONDecodeError, ValueError):
        messagebox.showerror(
            "Erro",
            f"O arquivo {arquivo} possui dados inválidos."
        )
        return []

    except OSError as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível ler o arquivo.\n{erro}"
        )
        return []


def salvar_dados(arquivo, dados):

    try:
        with open(arquivo, "w", encoding="utf-8") as arquivo_json:
            json.dump(
                dados,
                arquivo_json,
                indent=4,
                ensure_ascii=False
            )

        return True

    except (OSError, TypeError) as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar os dados.\n{erro}"
        )
        return False


produtos = carregar_dados(ARQUIVO_PRODUTOS)
movimentacoes = carregar_dados(ARQUIVO_MOVIMENTACOES)


def validar_produtos():

    for produto in produtos:

        campos = (
            "codigo",
            "nome",
            "quantidade",
            "estoque_minimo",
            "preco"
        )

        if not isinstance(produto, dict):
            return False

        for campo in campos:
            if campo not in produto:
                return False

        if (
            not isinstance(produto["codigo"], int)
            or not isinstance(produto["nome"], str)
            or not isinstance(produto["quantidade"], int)
            or not isinstance(produto["estoque_minimo"], int)
            or not isinstance(produto["preco"], (int, float))
        ):
            return False

        if (
            produto["codigo"] <= 0
            or produto["nome"].strip() == ""
            or produto["quantidade"] < 0
            or produto["estoque_minimo"] < 0
            or produto["preco"] <= 0
        ):
            return False

    codigos = [produto["codigo"] for produto in produtos]

    if len(codigos) != len(set(codigos)):
        return False

    return True


if not validar_produtos():
    messagebox.showerror(
        "Erro",
        "Existem produtos inválidos no arquivo JSON."
    )
    produtos = []


def limpar_campos():

    entrada_codigo.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_minimo.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)


def cadastrar_produto():

    codigo_texto = entrada_codigo.get().strip()
    nome = entrada_nome.get().strip()
    quantidade_texto = entrada_quantidade.get().strip()
    minimo_texto = entrada_minimo.get().strip()
    preco_texto = entrada_preco.get().strip()

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

    try:
        codigo = int(codigo_texto)
        quantidade = int(quantidade_texto)
        estoque_minimo = int(minimo_texto)
        preco = float(preco_texto.replace(",", "."))

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores numéricos válidos."
        )
        return

    if codigo <= 0:
        messagebox.showerror(
            "Erro",
            "O código deve ser maior que zero."
        )
        return

    if quantidade < 0 or estoque_minimo < 0:
        messagebox.showerror(
            "Erro",
            "Quantidade e estoque mínimo não podem ser negativos."
        )
        return

    if preco <= 0:
        messagebox.showerror(
            "Erro",
            "O preço deve ser maior que zero."
        )
        return

    for produto in produtos:

        if produto["codigo"] == codigo:
            messagebox.showerror(
                "Erro",
                "Já existe um produto com esse código."
            )
            return

    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "estoque_minimo": estoque_minimo,
        "preco": preco
    }

    produtos.append(novo_produto)

    if salvar_dados(ARQUIVO_PRODUTOS, produtos):

        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado com sucesso!"
        )

        limpar_campos()
        atualizar_tabela()

    else:
        produtos.remove(novo_produto)


def listar_produtos():

    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Lista de Produtos")
    janela_lista.geometry("750x400")
    janela_lista.configure(bg="#F1F4F9")

    tk.Label(
        janela_lista,
        text="Produtos Cadastrados",
        bg="#F1F4F9",
        fg="#172B4D",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tabela = ttk.Treeview(
        janela_lista,
        columns=(
            "codigo",
            "nome",
            "quantidade",
            "minimo",
            "preco"
        ),
        show="headings"
    )

    tabela.heading("codigo", text="Código")
    tabela.heading("nome", text="Nome")
    tabela.heading("quantidade", text="Quantidade")
    tabela.heading("minimo", text="Estoque Mínimo")
    tabela.heading("preco", text="Preço")

    tabela.column("codigo", width=70, anchor="center")
    tabela.column("nome", width=180)
    tabela.column("quantidade", width=100, anchor="center")
    tabela.column("minimo", width=120, anchor="center")
    tabela.column("preco", width=100, anchor="center")

    tabela.pack(fill="both", expand=True, padx=15, pady=10)

    for produto in produtos:

        tabela.insert(
            "",
            tk.END,
            values=(
                produto["codigo"],
                produto["nome"],
                produto["quantidade"],
                produto["estoque_minimo"],
                f"R$ {produto['preco']:.2f}"
            )
        )


def alterar_produto():

    codigo_texto = entrada_codigo.get().strip()

    if codigo_texto == "":
        messagebox.showwarning(
            "Atenção",
            "Digite o código do produto."
        )
        return

    try:
        codigo = int(codigo_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Código inválido."
        )
        return

    for produto in produtos:

        if produto["codigo"] == codigo:

            nome = entrada_nome.get().strip()
            quantidade_texto = entrada_quantidade.get().strip()
            minimo_texto = entrada_minimo.get().strip()
            preco_texto = entrada_preco.get().strip()

            if (
                nome == ""
                or quantidade_texto == ""
                or minimo_texto == ""
                or preco_texto == ""
            ):
                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos."
                )
                return

            try:
                quantidade = int(quantidade_texto)
                minimo = int(minimo_texto)
                preco = float(preco_texto.replace(",", "."))

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Digite valores numéricos válidos."
                )
                return

            if quantidade < 0 or minimo < 0 or preco <= 0:
                messagebox.showerror(
                    "Erro",
                    "Verifique a quantidade, o mínimo e o preço."
                )
                return

            dados_antigos = produto.copy()

            produto["nome"] = nome
            produto["quantidade"] = quantidade
            produto["estoque_minimo"] = minimo
            produto["preco"] = preco

            if salvar_dados(ARQUIVO_PRODUTOS, produtos):

                messagebox.showinfo(
                    "Sucesso",
                    "Produto alterado com sucesso!"
                )

                limpar_campos()
                atualizar_tabela()

            else:
                produto.update(dados_antigos)

            return

    messagebox.showwarning(
        "Não encontrado",
        "Produto não encontrado."
    )


def excluir_produto():

    codigo_texto = entrada_codigo.get().strip()

    if codigo_texto == "":
        messagebox.showwarning(
            "Atenção",
            "Digite o código do produto."
        )
        return

    try:
        codigo = int(codigo_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Código inválido."
        )
        return

    for produto in produtos:

        if produto["codigo"] == codigo:

            for movimento in movimentacoes:

                if movimento["codigo"] == codigo:
                    messagebox.showwarning(
                        "Atenção",
                        "Este produto possui histórico de movimentações.\n"
                        "Não é possível excluí-lo."
                    )
                    return

            confirmar = messagebox.askyesno(
                "Confirmar",
                "Deseja realmente excluir este produto?"
            )

            if confirmar:

                indice = produtos.index(produto)
                produtos.remove(produto)

                if salvar_dados(ARQUIVO_PRODUTOS, produtos):

                    messagebox.showinfo(
                        "Sucesso",
                        "Produto excluído com sucesso!"
                    )

                    limpar_campos()
                    atualizar_tabela()

                else:
                    produtos.insert(indice, produto)

            return

    messagebox.showwarning(
        "Não encontrado",
        "Produto não encontrado."
    )


def consultar_produto():

    codigo_texto = entrada_consulta.get().strip()

    if codigo_texto == "":
        messagebox.showwarning(
            "Atenção",
            "Digite o código do produto."
        )
        return

    try:
        codigo = int(codigo_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um código válido."
        )
        return

    for produto in produtos:

        if produto["codigo"] == codigo:

            messagebox.showinfo(
                "Produto encontrado",
                f"Código: {produto['codigo']}\n"
                f"Nome: {produto['nome']}\n"
                f"Quantidade: {produto['quantidade']}\n"
                f"Estoque mínimo: {produto['estoque_minimo']}\n"
                f"Preço: R$ {produto['preco']:.2f}"
            )

            return

    messagebox.showwarning(
        "Não encontrado",
        "Não existe produto com esse código."
    )


def consultar_por_nome():

    nome_busca = entrada_nome_consulta.get().strip().lower()

    if nome_busca == "":
        messagebox.showwarning(
            "Atenção",
            "Digite o nome do produto."
        )
        return

    encontrados = []

    for produto in produtos:

        if nome_busca in produto["nome"].lower():
            encontrados.append(produto)

    if len(encontrados) == 0:
        messagebox.showwarning(
            "Não encontrado",
            "Produto não encontrado."
        )
        return

    resultado = ""

    for produto in encontrados:

        resultado += (
            f"Código: {produto['codigo']}\n"
            f"Nome: {produto['nome']}\n"
            f"Quantidade: {produto['quantidade']}\n"
            f"Estoque mínimo: {produto['estoque_minimo']}\n"
            f"Preço: R$ {produto['preco']:.2f}\n\n"
        )

    messagebox.showinfo(
        "Produtos encontrados",
        resultado
    )


def registrar_movimentacao(codigo, quantidade, tipo):

    produto_encontrado = None

    for produto in produtos:

        if produto["codigo"] == codigo:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        messagebox.showerror(
            "Erro",
            "Produto não encontrado."
        )
        return

    if quantidade <= 0:
        messagebox.showerror(
            "Erro",
            "A quantidade deve ser maior que zero."
        )
        return

    quantidade_anterior = produto_encontrado["quantidade"]

    if tipo == "Saída" and quantidade > quantidade_anterior:
        messagebox.showerror(
            "Estoque insuficiente",
            "A saída não pode ser maior que o estoque atual."
        )
        return

    if tipo == "Entrada":
        quantidade_nova = quantidade_anterior + quantidade

    else:
        quantidade_nova = quantidade_anterior - quantidade

    nova_movimentacao = {
        "codigo": codigo,
        "produto": produto_encontrado["nome"],
        "tipo": tipo,
        "quantidade": quantidade,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    produto_encontrado["quantidade"] = quantidade_nova

    movimentacoes.append(nova_movimentacao)

    if not salvar_dados(ARQUIVO_PRODUTOS, produtos):

        produto_encontrado["quantidade"] = quantidade_anterior
        movimentacoes.remove(nova_movimentacao)
        return

    if not salvar_dados(ARQUIVO_MOVIMENTACOES, movimentacoes):

        produto_encontrado["quantidade"] = quantidade_anterior
        movimentacoes.remove(nova_movimentacao)

        salvar_dados(ARQUIVO_PRODUTOS, produtos)

        messagebox.showerror(
            "Erro",
            "Não foi possível registrar a movimentação.\n"
            "O estoque foi restaurado."
        )
        return

    messagebox.showinfo(
        "Sucesso",
        f"{tipo} registrada com sucesso!\n\n"
        f"Produto: {produto_encontrado['nome']}\n"
        f"Quantidade: {quantidade}\n"
        f"Estoque atual: {quantidade_nova}"
    )

    entrada_mov_codigo.delete(0, tk.END)
    entrada_mov_quantidade.delete(0, tk.END)

    atualizar_tabela()


def registrar_entrada():

    codigo_texto = entrada_mov_codigo.get().strip()
    quantidade_texto = entrada_mov_quantidade.get().strip()

    if codigo_texto == "" or quantidade_texto == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha o código e a quantidade."
        )
        return

    try:
        codigo = int(codigo_texto)
        quantidade = int(quantidade_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores inteiros válidos."
        )
        return

    registrar_movimentacao(
        codigo,
        quantidade,
        "Entrada"
    )


def registrar_saida():

    codigo_texto = entrada_mov_codigo.get().strip()
    quantidade_texto = entrada_mov_quantidade.get().strip()

    if codigo_texto == "" or quantidade_texto == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha o código e a quantidade."
        )
        return

    try:
        codigo = int(codigo_texto)
        quantidade = int(quantidade_texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores inteiros válidos."
        )
        return

    registrar_movimentacao(
        codigo,
        quantidade,
        "Saída"
    )


def listar_movimentacoes():

    janela_movimentacoes = tk.Toplevel(janela)
    janela_movimentacoes.title("Histórico de Movimentações")
    janela_movimentacoes.geometry("750x400")
    janela_movimentacoes.configure(bg="#F1F4F9")

    tk.Label(
        janela_movimentacoes,
        text="Histórico de Movimentações",
        bg="#F1F4F9",
        fg="#172B4D",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tabela_movimentos = ttk.Treeview(
        janela_movimentacoes,
        columns=(
            "codigo",
            "produto",
            "tipo",
            "quantidade",
            "data"
        ),
        show="headings"
    )

    tabela_movimentos.heading("codigo", text="Código")
    tabela_movimentos.heading("produto", text="Produto")
    tabela_movimentos.heading("tipo", text="Tipo")
    tabela_movimentos.heading("quantidade", text="Quantidade")
    tabela_movimentos.heading("data", text="Data")

    tabela_movimentos.column("codigo", width=70, anchor="center")
    tabela_movimentos.column("produto", width=170)
    tabela_movimentos.column("tipo", width=100, anchor="center")
    tabela_movimentos.column("quantidade", width=100, anchor="center")
    tabela_movimentos.column("data", width=150, anchor="center")

    tabela_movimentos.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    for movimento in movimentacoes:

        tabela_movimentos.insert(
            "",
            tk.END,
            values=(
                movimento["codigo"],
                movimento["produto"],
                movimento["tipo"],
                movimento["quantidade"],
                movimento["data"]
            )
        )


def produtos_estoque_baixo():

    janela_baixo = tk.Toplevel(janela)
    janela_baixo.title("Produtos com Estoque Baixo")
    janela_baixo.geometry("650x350")
    janela_baixo.configure(bg="#F1F4F9")

    tk.Label(
        janela_baixo,
        text="Produtos com Estoque Baixo",
        bg="#F1F4F9",
        fg="#172B4D",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tabela_baixo = ttk.Treeview(
        janela_baixo,
        columns=(
            "codigo",
            "nome",
            "quantidade",
            "minimo"
        ),
        show="headings"
    )

    tabela_baixo.heading("codigo", text="Código")
    tabela_baixo.heading("nome", text="Produto")
    tabela_baixo.heading("quantidade", text="Quantidade")
    tabela_baixo.heading("minimo", text="Estoque Mínimo")

    tabela_baixo.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    encontrados = 0

    for produto in produtos:

        if produto["quantidade"] <= produto["estoque_minimo"]:

            tabela_baixo.insert(
                "",
                tk.END,
                values=(
                    produto["codigo"],
                    produto["nome"],
                    produto["quantidade"],
                    produto["estoque_minimo"]
                )
            )

            encontrados += 1

    if encontrados == 0:
        messagebox.showinfo(
            "Estoque",
            "Nenhum produto está com estoque baixo."
        )


def atualizar_tabela():

    if "tabela_principal" not in globals():
        return

    for item in tabela_principal.get_children():
        tabela_principal.delete(item)

    for produto in produtos:

        tabela_principal.insert(
            "",
            tk.END,
            values=(
                produto["codigo"],
                produto["nome"],
                produto["quantidade"],
                produto["estoque_minimo"],
                f"R$ {produto['preco']:.2f}"
            )
        )


def gerar_relatorio():

    janela_relatorio = tk.Toplevel(janela)
    janela_relatorio.title("Relatório de Estoque")
    janela_relatorio.geometry("500x400")
    janela_relatorio.configure(bg="#F1F4F9")

    valor_total = 0
    quantidade_total = 0
    produtos_baixos = 0

    for produto in produtos:

        quantidade_total += produto["quantidade"]

        valor_total += (
            produto["quantidade"] * produto["preco"]
        )

        if produto["quantidade"] <= produto["estoque_minimo"]:
            produtos_baixos += 1

    tk.Label(
        janela_relatorio,
        text="RELATÓRIO DE ESTOQUE",
        bg="#F1F4F9",
        fg="#172B4D",
        font=("Arial", 19, "bold")
    ).pack(pady=25)

    quadro = tk.Frame(
        janela_relatorio,
        bg="white",
        padx=25,
        pady=25
    )
    quadro.pack(fill="both", expand=True, padx=25, pady=15)

    tk.Label(
        quadro,
        text=f"Total de produtos cadastrados: {len(produtos)}",
        bg="white",
        font=("Arial", 12)
    ).pack(anchor="w", pady=10)

    tk.Label(
        quadro,
        text=f"Quantidade total em estoque: {quantidade_total}",
        bg="white",
        font=("Arial", 12)
    ).pack(anchor="w", pady=10)

    tk.Label(
        quadro,
        text=f"Produtos com estoque baixo: {produtos_baixos}",
        bg="white",
        font=("Arial", 12)
    ).pack(anchor="w", pady=10)

    tk.Label(
        quadro,
        text=f"Valor total em estoque: R$ {valor_total:.2f}",
        bg="white",
        fg="#16A34A",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", pady=15)


def preencher_campos(event):

    selecionado = tabela_principal.selection()

    if not selecionado:
        return

    valores = tabela_principal.item(
        selecionado[0],
        "values"
    )

    entrada_codigo.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_minimo.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)

    entrada_codigo.insert(0, valores[0])
    entrada_nome.insert(0, valores[1])
    entrada_quantidade.insert(0, valores[2])
    entrada_minimo.insert(0, valores[3])

    produto = None

    for item in produtos:

        if item["codigo"] == int(valores[0]):
            produto = item
            break

    if produto:
        entrada_preco.insert(0, produto["preco"])


# CONFIGURAÇÃO VISUAL

janela.configure(bg="#F1F4F9")

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "TEntry",
    padding=7,
    font=("Arial", 10)
)

estilo.configure(
    "Azul.TButton",
    background="#2563EB",
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=10,
    borderwidth=0
)

estilo.map(
    "Azul.TButton",
    background=[("active", "#1D4ED8")]
)

estilo.configure(
    "Verde.TButton",
    background="#16A34A",
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=10,
    borderwidth=0
)

estilo.map(
    "Verde.TButton",
    background=[("active", "#15803D")]
)

estilo.configure(
    "Vermelho.TButton",
    background="#DC2626",
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=10,
    borderwidth=0
)

estilo.map(
    "Vermelho.TButton",
    background=[("active", "#B91C1C")]
)

estilo.configure(
    "Cinza.TButton",
    background="#475569",
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=10,
    borderwidth=0
)

estilo.map(
    "Cinza.TButton",
    background=[("active", "#334155")]
)

estilo.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=28
)

estilo.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold")
)


# CABEÇALHO

cabecalho = tk.Frame(
    janela,
    bg="#172B4D",
    height=100
)
cabecalho.pack(fill="x")

tk.Label(
    cabecalho,
    text="CONTROLE DE ESTOQUE",
    bg="#172B4D",
    fg="white",
    font=("Arial", 23, "bold")
).pack(pady=(18, 5))

tk.Label(
    cabecalho,
    text="Gerenciamento de produtos e mercadorias",
    bg="#172B4D",
    fg="#CBD5E1",
    font=("Arial", 11)
).pack()


# ÁREA PRINCIPAL

area_principal = tk.Frame(
    janela,
    bg="#F1F4F9"
)
area_principal.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=15
)


# CARTÃO DE CADASTRO

cartao_cadastro = tk.Frame(
    area_principal,
    bg="white",
    padx=20,
    pady=15
)
cartao_cadastro.pack(fill="x", pady=8)

tk.Label(
    cartao_cadastro,
    text="Cadastro de Produto",
    bg="white",
    fg="#172B4D",
    font=("Arial", 15, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 12)
)


tk.Label(
    cartao_cadastro,
    text="Código:",
    bg="white"
).grid(row=1, column=0, sticky="w", padx=5)

entrada_codigo = ttk.Entry(cartao_cadastro)
entrada_codigo.grid(row=2, column=0, padx=5, pady=5, sticky="ew")


tk.Label(
    cartao_cadastro,
    text="Nome do produto:",
    bg="white"
).grid(row=1, column=1, sticky="w", padx=5)

entrada_nome = ttk.Entry(cartao_cadastro)
entrada_nome.grid(row=2, column=1, padx=5, pady=5, sticky="ew")


tk.Label(
    cartao_cadastro,
    text="Quantidade:",
    bg="white"
).grid(row=3, column=0, sticky="w", padx=5, pady=(8, 0))

entrada_quantidade = ttk.Entry(cartao_cadastro)
entrada_quantidade.grid(row=4, column=0, padx=5, pady=5, sticky="ew")


tk.Label(
    cartao_cadastro,
    text="Estoque mínimo:",
    bg="white"
).grid(row=3, column=1, sticky="w", padx=5, pady=(8, 0))

entrada_minimo = ttk.Entry(cartao_cadastro)
entrada_minimo.grid(row=4, column=1, padx=5, pady=5, sticky="ew")


tk.Label(
    cartao_cadastro,
    text="Preço unitário (R$):",
    bg="white"
).grid(row=5, column=0, sticky="w", padx=5, pady=(8, 0))

entrada_preco = ttk.Entry(cartao_cadastro)
entrada_preco.grid(row=6, column=0, padx=5, pady=5, sticky="ew")


cartao_cadastro.columnconfigure(0, weight=1)
cartao_cadastro.columnconfigure(1, weight=1)


# BOTÕES DE CADASTRO

ttk.Button(
    cartao_cadastro,
    text="Cadastrar Produto",
    style="Verde.TButton",
    command=cadastrar_produto
).grid(
    row=7,
    column=0,
    columnspan=2,
    sticky="ew",
    pady=10
)


ttk.Button(
    cartao_cadastro,
    text="Alterar Produto",
    style="Azul.TButton",
    command=alterar_produto
).grid(
    row=8,
    column=0,
    padx=5,
    pady=5,
    sticky="ew"
)


ttk.Button(
    cartao_cadastro,
    text="Excluir Produto",
    style="Vermelho.TButton",
    command=excluir_produto
).grid(
    row=8,
    column=1,
    padx=5,
    pady=5,
    sticky="ew"
)


# CARTÃO DE MOVIMENTAÇÕES

cartao_movimento = tk.Frame(
    area_principal,
    bg="white",
    padx=20,
    pady=12
)
cartao_movimento.pack(fill="x", pady=8)

tk.Label(
    cartao_movimento,
    text="Entrada e Saída de Mercadorias",
    bg="white",
    fg="#172B4D",
    font=("Arial", 14, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 10)
)


tk.Label(
    cartao_movimento,
    text="Código do produto:",
    bg="white"
).grid(row=1, column=0, sticky="w", padx=5)

entrada_mov_codigo = ttk.Entry(cartao_movimento)
entrada_mov_codigo.grid(row=2, column=0, padx=5, pady=5, sticky="ew")


tk.Label(
    cartao_movimento,
    text="Quantidade:",
    bg="white"
).grid(row=1, column=1, sticky="w", padx=5)

entrada_mov_quantidade = ttk.Entry(cartao_movimento)
entrada_mov_quantidade.grid(row=2, column=1, padx=5, pady=5, sticky="ew")


cartao_movimento.columnconfigure(0, weight=1)
cartao_movimento.columnconfigure(1, weight=1)


ttk.Button(
    cartao_movimento,
    text="Registrar Entrada",
    style="Verde.TButton",
    command=registrar_entrada
).grid(
    row=3,
    column=0,
    padx=5,
    pady=8,
    sticky="ew"
)


ttk.Button(
    cartao_movimento,
    text="Registrar Saída",
    style="Vermelho.TButton",
    command=registrar_saida
).grid(
    row=3,
    column=1,
    padx=5,
    pady=8,
    sticky="ew"
)


# CARTÃO DE CONSULTAS

cartao_consulta = tk.Frame(
    area_principal,
    bg="white",
    padx=20,
    pady=12
)
cartao_consulta.pack(fill="x", pady=8)

tk.Label(
    cartao_consulta,
    text="Consultas e Relatórios",
    bg="white",
    fg="#172B4D",
    font=("Arial", 14, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 10)
)


tk.Label(
    cartao_consulta,
    text="Código:",
    bg="white"
).grid(row=1, column=0, sticky="w", padx=5)

entrada_consulta = ttk.Entry(cartao_consulta)
entrada_consulta.grid(row=2, column=0, padx=5, pady=5, sticky="ew")


tk.Label(
    cartao_consulta,
    text="Nome:",
    bg="white"
).grid(row=1, column=1, sticky="w", padx=5)

entrada_nome_consulta = ttk.Entry(cartao_consulta)
entrada_nome_consulta.grid(row=2, column=1, padx=5, pady=5, sticky="ew")


cartao_consulta.columnconfigure(0, weight=1)
cartao_consulta.columnconfigure(1, weight=1)


ttk.Button(
    cartao_consulta,
    text="Consultar Código",
    style="Azul.TButton",
    command=consultar_produto
).grid(row=3, column=0, padx=5, pady=5, sticky="ew")


ttk.Button(
    cartao_consulta,
    text="Consultar Código",
    style="Azul.TButton",
    command=consultar_produto
).grid(row=3, column=0, padx=5, pady=5, sticky="ew")


ttk.Button(
    cartao_consulta,
    text="Consultar Nome",
    style="Azul.TButton",
    command=consultar_por_nome
).grid(row=3, column=1, padx=5, pady=5, sticky="ew")


# BOTÃO PARA LISTAR TODOS OS PRODUTOS

ttk.Button(
    cartao_consulta,
    text="Listar Todos os Produtos",
    style="Cinza.TButton",
    command=listar_produtos
).grid(
    row=4,
    column=0,
    columnspan=2,
    padx=5,
    pady=5,
    sticky="ew"
)


# TABELA PRINCIPAL

cartao_tabela = tk.Frame(
    area_principal,
    bg="white",
    padx=15,
    pady=10
)
cartao_tabela.pack(fill="both", expand=True, pady=8)

tk.Label(
    cartao_tabela,
    text="Produtos em Estoque",
    bg="white",
    fg="#172B4D",
    font=("Arial", 14, "bold")
).pack(anchor="w", pady=8)


tabela_principal = ttk.Treeview(
    cartao_tabela,
    columns=(
        "codigo",
        "nome",
        "quantidade",
        "minimo",
        "preco"
    ),
    show="headings",
    height=5
)

tabela_principal.heading("codigo", text="Código")
tabela_principal.heading("nome", text="Produto")
tabela_principal.heading("quantidade", text="Quantidade")
tabela_principal.heading("minimo", text="Estoque Mínimo")
tabela_principal.heading("preco", text="Preço")

tabela_principal.column("codigo", width=65, anchor="center")
tabela_principal.column("nome", width=160)
tabela_principal.column("quantidade", width=90, anchor="center")
tabela_principal.column("minimo", width=110, anchor="center")
tabela_principal.column("preco", width=100, anchor="center")

tabela_principal.pack(fill="both", expand=True)

tabela_principal.bind(
    "<Double-1>",
    preencher_campos
)


# BOTÕES DE RELATÓRIO

quadro_botoes = tk.Frame(
    area_principal,
    bg="#F1F4F9"
)
quadro_botoes.pack(fill="x", pady=8)


ttk.Button(
    quadro_botoes,
    text="Listar Produtos",
    style="Cinza.TButton",
    command=listar_produtos
).pack(side="left", expand=True, fill="x", padx=3)


ttk.Button(
    quadro_botoes,
    text="Histórico",
    style="Azul.TButton",
    command=listar_movimentacoes
).pack(side="left", expand=True, fill="x", padx=3)


ttk.Button(
    quadro_botoes,
    text="Estoque Baixo",
    style="Vermelho.TButton",
    command=produtos_estoque_baixo
).pack(side="left", expand=True, fill="x", padx=3)


ttk.Button(
    quadro_botoes,
    text="Relatório",
    style="Verde.TButton",
    command=gerar_relatorio
).pack(side="left", expand=True, fill="x", padx=3)


# RODAPÉ

tk.Label(
    janela,
    text="Sistema de Controle de Estoque | Desenvolvido em Python",
    bg="#F1F4F9",
    fg="#64748B",
    font=("Arial", 9)
).pack(pady=8)


# CARREGAR PRODUTOS NA TABELA
atualizar_tabela()


# INICIAR SISTEMA
janela.mainloop()
