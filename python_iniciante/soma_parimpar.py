soma = 0
for i in range(1,11):
  num = int(input("Digite um número. "))
  soma += num
if soma % 2 == 0:
  print("este número é par ")
else:
  print("este número é impar")