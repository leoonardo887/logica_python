a = input("digite uma palavra. ")
vogal = "aeiouéáúíóãõàâêôûî"
contador = 0
for letra in a.lower():
  if letra in vogal:
    contador += 1
print("sua palavra tem",contador,"vogais")