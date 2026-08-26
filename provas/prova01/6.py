numeros = []
while True:
    valor = int(input("digite um número inteiro (zero para sair)"))
    if valor == 0:
        break
    numeros.append(valor)

while (len(numeros)) > 2:
    primeiro = numeros.pop(0)
    ultimo = numeros.pop()

print(f'o(s) valor(es) central(is) da lista são: {numeros}')