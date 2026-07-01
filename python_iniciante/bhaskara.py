a = float(input("Digite o número que acompanha x²: "))
b = float(input("Digite o número que acomapnha x: "))
c = float(input("Digite o termo independente: "))

delta = b**2 -4*a*c
bhaskara1 = (-b + delta**0.5) / (2*a)
bhaskara2 = (-b - delta**0.5) / (2*a)

print("O primeiro x vale", bhaskara1, "e o segundo vale", bhaskara2)