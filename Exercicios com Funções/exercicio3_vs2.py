altura = 1
largura = 18
n = "Usuário"
a = "Clientes"
c = "Fornecedores"
d = "Relatórios"

def linha():
    print(f'+{largura * '-'}+')                         #a parte de cima do quadrilatero 

def coluna1():
    for i in range(altura):                             #para cada numero em altura, printe | + largura vezes espaço + |
        print(f'|{n}{" " * (largura - len(n))}|')

def coluna2():
    for i in range(altura):                             #printará "a", depois com o len ele irá contar a quantidade de letras em "a" (login) e subtrairá da largura.
        print(f'|{a}{" " * (largura - len(a))}|')

def coluna3():
    for i in range(altura):                             
        print(f'|{c}{" " * (largura - len(c))}|')

def coluna4():
    for i in range(altura):                             
        print(f'|{d}{" " * (largura - len(d))}|')

print(linha(),coluna1(),linha(), coluna2(), linha(), coluna3(), linha(), coluna4(), linha())