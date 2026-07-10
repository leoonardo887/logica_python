def linhas():
    """Cria uma linha +-----+"""
    print(f"+{largura*'-'}+")

def colunas():
    """Cria duas colunas com uma palavra no centro | palavra |"""
    for linha in range(altura):
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            print(f"|{largura*" "}|")

def menu():
    print("\nMenu: ")
    print("0 - Adicionar Filme (Opcional)")
    print("1 - Quantidade total de filmes")
    print("2- Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

altura = 1
largura = 40

palavras = ("Adicionar Filme - 0", "Quantidade total de filmes - 1", "Informações de um filme pelo titulo - 2", "Filmes de um diretor específico - 3", "Filmes de um gênero específico - 4", "Média de duração dos filmes - 5", "Sair - ")

titulos = []
diretores = []
generos = []
duracao = []

for palavra in palavras:
    linhas()
    colunas()
linhas()

while True:

    opcao = int(input("O que você deseja fazer: "))

    if opcao == 0:
        while True:
            titulo = input("Escreva o título do filme: ")

            if titulo == "":
                break

            titulos.append(titulo)

            diretor = input("Escreva o nome do diretor: ")

            if diretor == "":
                break

            diretores.append(diretor)

            genero = input("Escreva o gênero do filme: ")

            if genero == "":
                break

            generos.append(genero)

            tempo = input("Escreva quantos minutos de duração tem o filme: ")

            if tempo == "":
                break

            duracao.append(tempo)

        with open("Arq_Filmes.txt", "w") as f:
            for i in range(len(titulos)):
                f.write(f"{titulos[i]} - {diretores[i]} - {generos[i]} - {duracao[i]}\n")

        continue

    if  opcao == 1:
        print(len(titulos))
        continue

    if opcao == 2:

        titulo_procurado = input("Digite o titulo do filme:")

        with open("Arq_Filmes.txt", "r") as f:


        continue