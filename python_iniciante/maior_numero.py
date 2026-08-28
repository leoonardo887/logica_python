# CÓDIGO PARA SABER O MAIOR NÚMERO ENTRE OS DIGITADOS

maior = 0

for i in range(3):
    num = int(input("Digite um número: "))

    if num > maior:
        maior = num

print("O maior número é", maior)