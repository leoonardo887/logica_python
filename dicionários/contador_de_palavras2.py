#jeito do professor
dicionario = {}
frase = input("digite uma frase: ")
lista_palavras = frase.split()
for palavra in lista_palavras:      #o primeiro valor(palavra) é sempre a chave, a segunda é o valor dentro da chave
  if palavra not in dicionario:
    dicionario[palavra] = 1
  else:
    dicionario[palavra] += 1
                                                      #poderia fazer o print aqui e ficaria {xxx: y zzz: w ...}
for palavra, quantidade in dicionario.items():        #jeito de mudar o print
  print(f'{palavra}: {quantidade}')

dif = len(dicionario)