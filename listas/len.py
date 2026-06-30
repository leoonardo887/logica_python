#pôr números em uma lista e após fazer a média deles
lista = []
x = 0
while x < 5:
  valor = int(input("Qual número deseja adicionar à lista? "))
  lista.append(valor)
  x += 1
soma = sum(lista)
media = soma / len(lista)
print(media)

#LEN é a quantidade de itens que tem dentro da lista.