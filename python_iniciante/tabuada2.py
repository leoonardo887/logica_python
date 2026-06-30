t = 1
while t <= 10:
  t = float(input("Digite um número: "))
  if t == 0.1:
    print("Programa finalizado!")
    break
  a = input("digite a operação(+, -,* ou /)")
  n = 1
  print(f'Tabuada de {t}:')
  print(f'='*15)
  while n <= 10:
    if a == "+":
      print(f'{t} + {n} = {t+n}')
    elif a == "-":
      print(f'{t} - {n} = {t-n}')
    elif a == "*":
      print(f'{t} x {n} = {t*n}')
    elif a == "/":
      print(f'{t} : {n} = {t/n}')
    n += 1
  t += 1