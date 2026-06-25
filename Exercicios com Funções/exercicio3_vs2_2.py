altura = 3
largura = 18

palavras = ("Usuários", "Clientes", "Fornecedores", "Relatórios")

def linhas():
    print(f'+{largura * '-'}+')   

def colunas():
    for linha in range(altura):
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            print(f"|{largura * " "}|")

for palavra in palavras:
    linhas()
    colunas()
    linhas()