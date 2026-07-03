tabuleiro = []

linhas = 3
colunas = 3

jogador = "X"
soma = 0

for i in range(linhas):
  linha = []
  for j in range(colunas):
    linha.append(" ")
  tabuleiro.append(linha)

while True:
    linha_escolhida = int(input("Digite que linha você deseja (1-3): "))
    coluna_escolhida = int(input("Digite que coluna você deseja (1-3): "))

    if tabuleiro[linha_escolhida-1][coluna_escolhida-1] != " ":
       print("Este local já está ocupado. ")
       continue

    tabuleiro[linha_escolhida-1][coluna_escolhida-1] = jogador


    soma = 0

    for linha in tabuleiro:
        for elemento in linha:
            print(f'[{elemento}]', end="\t")
            if elemento != " ":
                soma += 1
        print()

    for i in range(3):
       if tabuleiro[i][0] == tabuleiro [i][1] == tabuleiro [i][2] != " ":
          print('O jogador', jogador, "venceu!")
          exit()
       
    for i in range(3):
       if tabuleiro[0][i] == tabuleiro [1][i] == tabuleiro [2][i] != " ":
          print('O jogador', jogador, "venceu!")
          exit()

    for i in range(3):
       if tabuleiro[0][0] == tabuleiro[2][2] == tabuleiro [1][1] != " ":
          print("O jogador", jogador, "Venceu!")
          exit()

    for i in range(3):
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            print("O jogador", jogador, "venceu!")
            exit()

    if soma == 9:
        print("Empate")
        exit()
    
    if jogador == "X":
       jogador = "O"                    #momento em que ele alterna entre o jogador X e O
    else:
       jogador = "X"