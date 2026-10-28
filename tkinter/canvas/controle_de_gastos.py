import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

ARQUIVO = "movimentacoes.json"
movimentacoes = []


# CORES
FUNDO = "#D1CDCD"
AZUL = "#0A3352"
VERDE = "#16803C"
VERMELHO = "#C0392B"
BRANCO = "#FFFFFF"


# CARREGAR DADOS
def carregar_dados():
    if not os.path.exists(ARQUIVO):     # verifica se o arquivo existe.
        salvar_dados()                  #se não, ele cria o arquivo
        return

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if isinstance(dados, list):             #O programa verifica se os dados são uma lista.
            movimentacoes.extend(dados)         #Se forem, coloca todas as movimentações encontradas dentro da lista movimentacoes.
                                                #Assim, os registros aparecem novamente no programa.
        else:
            messagebox.showerror(
                "Erro", "O arquivo JSON não contém uma lista válida."
            )

    except (json.JSONDecodeError, OSError):
        messagebox.showerror(
            "Erro", "Não foi possível ler o arquivo JSON."
        )


# SALVAR DADOS
def salvar_dados():         #responsável por salvar os dados em um arquivo
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(
                movimentacoes,                      #o que vai guardar
                arquivo,                            #lugar onde vai guardar
                ensure_ascii=False,                 #mantém os caracteres especiais legíveis
                indent=4                            #organiza
            )
        return True

    except OSError:
        messagebox.showerror(
            "Erro", "Não foi possível salvar os dados."
        )
        return False


# FORMATAR DINHEIRO
def dinheiro(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")         #organizar como dinheiro aparecerá na janela
    texto = texto.replace("X", ".")
    return f"R$ {texto}"


# GERAR IDENTIFICADOR
def gerar_id():
    if not movimentacoes:
        return 1                                           #cálculo de ordem das movimentações
    return max(item["id"] for item in movimentacoes) + 1


# CALCULAR SALDO
def calcular_saldo():
    saldo = 0

    for item in movimentacoes:
        if item["tipo"] == "Receita":
            saldo += item["valor"]                    #fórmula do saldo
        elif item["tipo"] == "Despesa":
            saldo -= item["valor"]

    return saldo


# ATUALIZAR SALDO NA TELA
def atualizar_saldo():
    saldo = calcular_saldo()
    texto_saldo.config(text=dinheiro(saldo))

    if saldo < 0:
        texto_saldo.config(fg=VERMELHO)             #caso o saldo esteja negativo, o saldo aparece vermelho na janela, caso contrário, verde.
    else:
        texto_saldo.config(fg=VERDE)


def atualizar_tabela():
    for item in tabela.get_children():  #pega os itens que já estão na tabela.
        tabela.delete(item)             #apaga cada item antigo da tabela para evitar duplicações.

    for item in movimentacoes:          #percorre todas as movimentações salvas na lista.
        tabela.insert(                  #insere as informações na tabela
            "",
            "end",                      #indica que o item será colocado no final
            iid=str(item["id"]),        #indica o id de cada um: 1, 2,...
            values=(                    #itens
                item["id"],
                item["data"],
                item["tipo"],
                item["descricao"],
                dinheiro(item["valor"])
            )
        )

    atualizar_saldo()


# LIMPAR CAMPOS
def limpar_campos():                        #Essa função limpa os campos do formulário depois de cadastrar uma movimentação.
    entrada_descricao.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    entrada_descricao.focus()


# ADICIONAR RECEITA OU DESPESA
def adicionar_movimentacao():
    descricao = entrada_descricao.get().strip()
    valor_texto = entrada_valor.get().strip().replace(",", ".")     #troca a vírgula por ponto, permitindo digitar, por exemplo, 25,50.
    tipo = escolha_tipo.get()

    if not descricao:
        messagebox.showwarning(
            "Atenção", "Digite a descrição da movimentação."
        )
        entrada_descricao.focus()
        return

    if not valor_texto:
        messagebox.showwarning(
            "Atenção", "Digite o valor da movimentação."
        )
        entrada_valor.focus()
        return

    try:
        valor = float(valor_texto)
    except ValueError:
        messagebox.showerror(
            "Erro", "Digite um valor numérico válido."
        )
        entrada_valor.focus()
        return

    if valor <= 0:
        messagebox.showwarning(
            "Atenção", "O valor deve ser maior que zero."
        )
        entrada_valor.focus()
        return

    if tipo not in ("Receita", "Despesa"):
        messagebox.showwarning(
            "Atenção", "Selecione Receita ou Despesa."
        )
        return

    movimentacao = {                            #como vai ficar o dicionario
        "id": gerar_id(),
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    movimentacoes.append(movimentacao)        #adiciona o dicionário à lista

    if salvar_dados():
        atualizar_tabela()
        limpar_campos()
        messagebox.showinfo(
            "Sucesso", f"{tipo} cadastrada com sucesso!"
        )
    else:
        movimentacoes.pop()


# EXCLUIR MOVIMENTAÇÃO
def excluir_movimentacao():
    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showwarning(
            "Atenção",
            "Selecione uma movimentação na tabela para excluir."
        )
        return

    identificador = int(selecionado[0])

    confirmar = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja excluir a movimentação ID {identificador}?"
    )

    if not confirmar:
        return

    for item in movimentacoes:
        if item["id"] == identificador:
            movimentacoes.remove(item)

            if salvar_dados():
                atualizar_tabela()
                messagebox.showinfo(
                    "Sucesso", "Movimentação excluída com sucesso!"
                )
            else:
                movimentacoes.append(item)
                atualizar_tabela()

            return


# GERAR RELATÓRIO
def gerar_relatorio():          #relatório de todos os ganhos e gastos
    total_receitas = 0
    total_despesas = 0

    for item in movimentacoes:
        if item["tipo"] == "Receita":
            total_receitas += item["valor"]
        elif item["tipo"] == "Despesa":
            total_despesas += item["valor"]

    saldo = total_receitas - total_despesas

    mensagem = (
        "RELATÓRIO FINANCEIRO\n\n"
        f"Total de receitas: {dinheiro(total_receitas)}\n"
        f"Total de despesas: {dinheiro(total_despesas)}\n"
        f"Saldo atual: {dinheiro(saldo)}\n"
        f"Quantidade de movimentações: {len(movimentacoes)}"
    )

    messagebox.showinfo("Relatório Financeiro", mensagem)


# JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Controle Financeiro Pessoal")
janela.geometry("1000x650")
janela.minsize(850, 550)
janela.configure(bg=FUNDO)


# CARREGAR DADOS ANTES DE MONTAR A TELA
carregar_dados()


# CABEÇALHO
cabecalho = tk.Frame(janela, bg=AZUL, height=90)
cabecalho.pack(fill="x")
cabecalho.pack_propagate(False)

tk.Label(
    cabecalho,
    text="Controle Financeiro Pessoal",
    font=("Arial", 22, "bold"),
    bg=AZUL,
    fg=BRANCO
).pack(pady=(12, 0))

tk.Label(
    cabecalho,
    text="Gerencie suas receitas e despesas",
    font=("Arial", 11),
    bg=AZUL,
    fg=BRANCO
).pack()


# ÁREA PRINCIPAL
principal = tk.Frame(janela, bg=FUNDO)
principal.pack(fill="both", expand=True, padx=20, pady=15)

principal.columnconfigure(0, weight=1)
principal.columnconfigure(1, weight=3)
principal.rowconfigure(0, weight=1)


# PAINEL DE CADASTRO
painel = tk.LabelFrame(
    principal,
    text=" Nova movimentação ",
    font=("Arial", 12, "bold"),
    bg=BRANCO,
    padx=15,
    pady=15
)
painel.grid(row=0, column=0, sticky="nsew", padx=(0, 15))

tk.Label(
    painel, text="Descrição:", bg=BRANCO, font=("Arial", 10)
).pack(anchor="w", pady=(5, 4))

entrada_descricao = tk.Entry(painel, font=("Arial", 11))
entrada_descricao.pack(fill="x", pady=(0, 12))

tk.Label(
    painel, text="Valor (R$):", bg=BRANCO, font=("Arial", 10)
).pack(anchor="w", pady=(0, 4))

entrada_valor = tk.Entry(painel, font=("Arial", 11))
entrada_valor.pack(fill="x", pady=(0, 12))

tk.Label(
    painel, text="Tipo:", bg=BRANCO, font=("Arial", 10)
).pack(anchor="w", pady=(0, 4))

escolha_tipo = ttk.Combobox(
    painel,
    values=["Receita", "Despesa"],
    state="readonly",
    font=("Arial", 10)
)
escolha_tipo.pack(fill="x", pady=(0, 15))
escolha_tipo.set("Receita")


# BOTÃO CADASTRAR
tk.Button(
    painel,
    text="Adicionar movimentação",
    command=adicionar_movimentacao,
    bg=AZUL,
    fg=BRANCO,
    activebackground="#174A70",
    activeforeground=BRANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=9
).pack(fill="x", pady=(0, 10))


# BOTÃO EXCLUIR
tk.Button(
    painel,
    text="Excluir selecionada",
    command=excluir_movimentacao,
    bg=VERMELHO,
    fg=BRANCO,
    activebackground="#A93226",
    activeforeground=BRANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=9
).pack(fill="x", pady=(0, 10))


# BOTÃO RELATÓRIO
tk.Button(
    painel,
    text="Gerar relatório",
    command=gerar_relatorio,
    bg=VERDE,
    fg=BRANCO,
    activebackground="#116530",
    activeforeground=BRANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=9
).pack(fill="x", pady=(0, 15))


# PAINEL DA TABELA E DO SALDO
painel_direito = tk.Frame(principal, bg=FUNDO)
painel_direito.grid(row=0, column=1, sticky="nsew")
painel_direito.rowconfigure(1, weight=1)
painel_direito.columnconfigure(0, weight=1)


# CARTÃO DE SALDO
cartao_saldo = tk.Frame(painel_direito, bg=BRANCO, padx=15, pady=10)
cartao_saldo.grid(row=0, column=0, sticky="ew", pady=(0, 12))

tk.Label(
    cartao_saldo,
    text="SALDO ATUAL",
    font=("Arial", 10, "bold"),
    bg=BRANCO,
    fg="#64748B"
).pack(anchor="w")

texto_saldo = tk.Label(
    cartao_saldo,
    text="R$ 0,00",
    font=("Arial", 23, "bold"),
    bg=BRANCO,
    fg=VERDE
)
texto_saldo.pack(anchor="w")


# TABELA DE MOVIMENTAÇÕES
painel_tabela = tk.LabelFrame(
    painel_direito,
    text=" Movimentações registradas ",
    font=("Arial", 12, "bold"),
    bg=BRANCO,
    padx=10,
    pady=10
)
painel_tabela.grid(row=1, column=0, sticky="nsew")
painel_tabela.rowconfigure(0, weight=1)
painel_tabela.columnconfigure(0, weight=1)

colunas = ("id", "data", "tipo", "descricao", "valor")

tabela = ttk.Treeview(
    painel_tabela,
    columns=colunas,
    show="headings",
    selectmode="browse"
)

tabela.heading("id", text="ID")
tabela.heading("data", text="Data/Hora")
tabela.heading("tipo", text="Tipo")
tabela.heading("descricao", text="Descrição")
tabela.heading("valor", text="Valor")

tabela.column("id", width=45, anchor="center")
tabela.column("data", width=125, anchor="center")
tabela.column("tipo", width=80, anchor="center")
tabela.column("descricao", width=150, anchor="w")
tabela.column("valor", width=100, anchor="e")

barra = ttk.Scrollbar(
    painel_tabela,
    orient="vertical",
    command=tabela.yview
)
tabela.configure(yscrollcommand=barra.set)

tabela.grid(row=0, column=0, sticky="nsew")
barra.grid(row=0, column=1, sticky="ns")


# RODAPÉ
tk.Label(
    janela,
    text="Os dados são salvos automaticamente em movimentacoes.json",
    bg=FUNDO,
    fg="#64748B",
    font=("Arial", 9)
).pack(pady=(0, 10))

# EXIBIR DADOS INICIAIS
atualizar_tabela()


janela.mainloop()