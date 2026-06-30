#jeito do professor
numero = int(input("digite um número: "))
encontrado = False
for i in range(5):
  for j in range(5):
    if matriz[i][j]==numero:
      print(f'O número {numero} existe na posição [{i+1},{j+1}]' )
      encontrado = True
if not encontrado:
  print(f'o número {numero} não existe na matriz')