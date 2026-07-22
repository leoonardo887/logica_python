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

def adicionar_filme():
    """Adiciona filmes ao Arq_Filmes.txt com todas as suas informações"""
    while True:

            titulo = input("Escreva o título do filme: (Digite *Pare* para sair)")

            if titulo == "Pare":
                break

            diretor = input("Escreva o nome do diretor: ")
            genero = input("Escreva o gênero do filme: ")
            tempo = input("Escreva quantos minutos de duração tem o filme: ")

            with open("Arq_Filmes.txt", "a", encoding="utf-8") as f:
                f.write(f"{titulo} - {diretor} - {genero} - {tempo}\n")

    print("Filme adicionado com sucesso!")

def quantidade_de_filmes():
        """Conta e imprime a quantidade de filmes presentes no arquivo."""
        with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
            quantidade = len(f.readlines())
            print(f"Quantidade de filmes: {quantidade}")

def informacao_filme():
    """Imprime todas as principais informações dos filmes arquivados."""
    titulo_procurado = input("Digite o titulo do filme: ")

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False

        for linha in f:
            dados = linha.strip().split(" - ")

            if dados[0].lower() == titulo_procurado.lower():
                print(f"Título: {dados[0]}")
                print(f"Diretor: {dados[1]}")
                print(f"Gênero: {dados[2]}")
                print(f"Duração: {dados[3]} minutos")
                encontrado = True
                break

        if not encontrado:
            print("Filme não encontrado.")

def diretor_filme():
    """Imprime todos os filmes arquivados dirigidos pelo diretor escolhido."""
    diretor_procurado = input("Digite o diretor do filme: ")

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False

        for linha in f:
            dados = linha.strip().split(" - ")

            if dados[1].lower() == diretor_procurado.lower():
                print(f"Título: {dados[0]}")
                encontrado = True

        if not encontrado:
                print("Nenhum filme encontado no nome desse diretor.")

def genero_filme():
    """Imprime todos os filmes arquivados que pertençam ao gênero escolhido."""
    genero_procurado = input("Digite o gênero do filme: ")

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False

        for linha in f:
            dados = linha.strip().split(" - ")

            if dados[2].lower() == genero_procurado.lower():
                print(f"Título: {dados[0]}")
                encontrado = True

        if not encontrado:
                print("Nenhum filme encontado com esse gênero.")

def media_filmes():
    """Calcula a média de duração em minutos de todos os filmes arquivados."""
    soma_duracao = 0
    quantidade = 0

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        for linha in f:
            dados =linha.strip().split(" - ")

            duracao = int(dados[3])
            soma_duracao += duracao
            quantidade += 1

        if quantidade > 0:
            media = soma_duracao / quantidade
            print(f"A média de duração dos filmes é de {media:.2f} minutos.")
        else:
            print("Não existem filmes arquivados.")

altura = 1
largura = 40

palavras = ("Adicionar Filme - 0", "Quantidade total de filmes - 1", "Informações de um filme pelo titulo - 2", "Filmes de um diretor específico - 3", "Filmes de um gênero específico - 4", "Média de duração dos filmes - 5", "Sair - 6")

if __name__ == "__main__":

    for palavra in palavras:
        linhas()
        colunas()
    linhas()

while True:

    opcao = input("O que você deseja fazer: ")        #Menu. 

    if opcao == "0":
        adicionar_filme()           #onde chamam as funções. 
    elif  opcao == "1":
        quantidade_de_filmes()
    elif opcao == "2":
        informacao_filme()
    elif opcao == "3":
        diretor_filme()
    elif opcao == "4":
        genero_filme()
    elif opcao == "5":
        media_filmes()
    elif opcao == "6":
        break
    elif opcao > "6":
        print("Número maior que o desejado. (0-6)")
    elif opcao < "0":
        print("Número menor que o desejado. (0-6)")