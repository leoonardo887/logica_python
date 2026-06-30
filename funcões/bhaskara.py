def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    bhaskara1 = (-b + delta ** 0.5) / (2 * a)
    bhaskara2 = (-b - delta ** 0.5) / (2 * a)

a = float(input("Digite o valor do número que acompanha o x²: "))
b = float(input("Digite o valor do número que acompanha o x: "))
c = float(input("Digite o valor do número independente: "))


print(bhaskara(a, b, c))