print(f'{"="*5} calculadora de Pitágoras {"="*5}')
print("Digite 1 caso queira calcular a hipotenusa. ")
print("Digite 2 caso queira calcular o valor de um cateto. ")
calculo = int(input("Digite. "))

if calculo > 2:
  print("Número digitado errado. ")

elif calculo == 1:
  cat1 = float(input("Quanto vale o primeiro cateto? "))
  cat2 = float(input("Quanto vale o segundo cateto? "))
  hip1 = (cat1**2 + cat2**2)**0.5
  print("A hipotenusa vale: ", hip1)

else:
  hip2 = float(input("Quanto vale a hipotenusa? "))
  cat3 = float(input("Quanto vale o cateto? "))
  cat4 = (hip2**2 - cat3**2)**0.5
  print("O cateto vale: ", cat4)