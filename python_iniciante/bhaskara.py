A = float(input("Qual o número que multiplica x ao quadrado? "))
B = float(input("Qual o número que multiplica x? "))
C =float(input("Qual o número que multiplica x^0? "))
delta = ((B**2 - 4*A*C)**0.5)
bhaskara1 = (-B + (delta))/(2*A)
bhaskara2 = (-B - (delta))/(2*A)

print(f'A primeira raiz da equação é {bhaskara1} e a segunda raiz é {bhaskara2}.')