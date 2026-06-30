a = input("digite uma palavra: ")
contador_vogais = 0
contador_consoantes = 0
vogal = "aeiouAEIOUéáóúíà"
for letra in a:
  if letra in vogal:
    contador_vogais += 1
  else:
    contador_consoantes += 1
print(f'sua palavra tem {contador_vogais} vogais, e {contador_consoantes} consoantes')