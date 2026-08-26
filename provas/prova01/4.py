soma = 0

for i in range(4):
    notas = float(input("Digite suas notas (0 - 10) "))
    soma += notas

media = soma / 4

if media >= 7:
    print("Aprovado! ")
elif media >= 5:
    print("Terá que fazer um exame. ")
else:
    print("Reprovado. ")