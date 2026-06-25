altura = int(input("Quanto de altura você quer seu retângulo? "))
largura = int(input("Quanto de largura você quer seu retângulo? "))

def linha():
    print("+", end="")
    for c in range(largura):
        print('-',end="")
    print("+")

def corpo():
    for l in range(altura):
        print("|", end="")
        for c in range(largura):
           print(" ", end="")
        print("|")

print(linha(),corpo(),linha())