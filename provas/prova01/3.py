
#minimo 8 letras, uma maiuscula, uma minuscula e um numero. 

numeros = "0123456789"
letras_mai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_min = "abcdefghijklmnopqrstuvwxyz"

contador_car = 0
contador_letra_mai = 0
contador_letra_min = 0
numero = 0
 
while True:
    senha = input("Digite uma senha. ")

    for letra in senha:
        contador_car += 1
        if letra in letras_mai:
            contador_letra_mai += 1
        if letra in letras_min:
            contador_letra_min += 1
        if letra in numeros:
            numero += 1
    
    if contador_car < 8:
        print("Senha fraca! mínimo de 8 caracteres. ")
        continue
    elif contador_letra_mai == 0:
        print("Senha fraca! mínimo de uma letra maiúscula. ")
        continue
    elif contador_letra_min == 0:
        print("Senha fraca! mínimo de uma letra minúscula. ")
        continue
    elif numero == 0:
        print("Senha fraca! Digite pelo menos um número. ")
        continue
    else:
        print("Senha forte!")
        break