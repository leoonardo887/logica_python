def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    bhaskara1 = (-b + delta ** 0.5) / (2 * a)
    bhaskara2 = (-b - delta ** 0.5) / (2 * a)
    return bhaskara1, bhaskara2

a = float(input("Digite o valor do número que acompanha o x²: "))
b = float(input("Digite o valor do número que acompanha o x: "))
c = float(input("Digite o valor do número independente: "))

bhaskara1, bhaskara2 = bhaskara(a, b, c)

print("O primeiro x vale", bhaskara1, "e o segundo x vale", bhaskara2)