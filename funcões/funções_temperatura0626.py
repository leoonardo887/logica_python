#aula 25/06/26

def fahrenheit_para_celsius(f):
    """Converte temperatura de fahrenheit para celsius"""
    celsius = (f - 32) * 5/9
    return celsius
while True:
    temp = float(input("Digite uma temperatura em Fahrenheit. (printe 0 para sair)"))
    celsius = fahrenheit_para_celsius(temp)
    print(celsius)
    if temp == 0:
        break