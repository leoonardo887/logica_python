with open("exemplo8/7/26.txt", "r") as f:
    linhas = f.readlines()
    for linha in linhas:
        print(linha.strip())
        print(f.readlines(0))

#o readlines joga todo o conteúdo para uma lista.

#O método .strip() em Python é usado para remover caracteres do início e do fim de uma string. Por padrão, ele remove espaços em branco, que incluem:

#Espaços ( )
#Quebras de linha (\n)
#Tabulações (\t)