numeros = []
while True:
  valor = int(input("digite um número (zero para sair)"))
  if valor == 0:
    break
  numeros.append(valor)

for i in numeros:      #para cada valor dentro de numeros (lista) printe ele
  print("lista completa: ", i)