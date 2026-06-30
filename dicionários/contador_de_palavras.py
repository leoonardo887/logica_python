#um programa que peça uma frase(com palavras repetidas) ao usuario. conte quantas vezes cada palavra aparece.armazene em um dicionario.exiba as palavras e quantas ocorrencias.
chave = {}

texto = input("Escreva uma frase e repita palavras nela. ")
palavras = texto.split()  #.SPLIT SEPARA CADA PALAVRA DENTRO DO TEXTO

for palavra in palavras:
  if palavra in chave:
    chave[palavra] += 1        #
  else:
    chave[palavra] = 1         #aqui ele pega a palavra, poe dentro da chave e iguala ela a um


print(chave)