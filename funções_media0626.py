def calcular_media():
    """Calcula média"""
    soma = 0
    for numero in numeros:
        soma += numero 
    media = soma / len(numeros)
    return media

numeros = []
qtd_numeros = int(input("De quantos números você quer calcular a média?"))

for i in range(qtd_numeros):
    numero = int(input("Qual número deseja adicionar à média? "))
    numeros.append(numero)

print(calcular_media())
 
