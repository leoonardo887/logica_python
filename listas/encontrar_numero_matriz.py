#meu jeito
matriz = ([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25])
num = int(input("digite um número de 1 à 25: "))
encontrado = False
for linha in range(len(matriz)):
  for coluna in range(len(matriz[linha])):
    if matriz[linha][coluna] == num:
      print(f'número encontrado na posição [{linha+1}][{coluna+1}]')
      encontrado = True
if not encontrado:
  print("número",num ,"não encontrado na matriz")