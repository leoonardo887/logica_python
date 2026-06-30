numeros = []
while True:
  valor = int(input("Digite um número (zero para sair): "))
  if valor == 0:
    break
  numeros.append(valor)
                                    #max é o número máximo da lista
                                    #min é o número mínimo.
for i in numeros:                   #para cada valor dentro de numeros (lista) printe ele
  print("Lista completa: ", i)
print("O maior número é", max(numeros), "e o menor é", min(numeros))