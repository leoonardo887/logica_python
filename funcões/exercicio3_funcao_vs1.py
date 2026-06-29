altura = int(input("Quanto de altura você quer seu retângulo? "))
largura = int(input("Quanto de largura você quer seu retângulo? "))

def linha():
    print(f'+{largura * '-'}+')                         #a parte de cima do quadrilatero 

def coluna():
    for i in range(altura):                             #para cada numero em altura, printe | + largura vezes espaço + |
        print(f'|{largura * ' '}|')

print(linha(),coluna(),linha())                         #a parte de baixo do quadrilatero 