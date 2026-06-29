altura = 1
largura = 18

def linha():
    print(f"+{'-' * largura}+")

def coluna(texto):
    for i in range(altura):
        print(f"|{texto}{' ' * (largura - len(texto))}|")

linha()
coluna("Usuário")
linha()
coluna("Clientes")
linha()
coluna("Fornecedores")
linha()
coluna("Relatórios")
linha()