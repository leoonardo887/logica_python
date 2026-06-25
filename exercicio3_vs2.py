altura = 1
largura = 18
n = "Usuário"
a = "login"
z = "Criar conta"

def linha():
    print(f'+{largura * '-'}+')                         #a parte de cima do quadrilatero 

def coluna1():
    for i in range(altura):                             #para cada numero em altura, printe | + largura vezes espaço + |
        print(f'|{n}{" " * (largura - len(n))}|')

def coluna2():
    for i in range(altura):                             #para cada numero em altura, printe | + largura vezes espaço + |
        print(f'|{a}{" " * (largura - len(a))}|')

def coluna3():
    for i in range(altura):                             #para cada numero em altura, printe | + largura vezes espaço + |
        print(f'|{z}{" " * (largura - len(z))}|')


print(linha(),coluna1(),linha(), coluna2(), linha(), coluna3(), linha())                         #a parte de baixo do quadrilatero 