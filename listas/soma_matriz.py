matriz = [[1,2,3],[4,5,6],[7,8,9]]
print("matriz 3x3\n")
soma = 0
for linha in matriz:
  for elemento in linha:
    print(f'[{elemento}]\t', end="")
    soma += elemento
  print()
print('a soma deles é',soma)