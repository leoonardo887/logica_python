def menu():
    print("\n0 - Adicionar filme")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


def adicionar_filme():
    while True:
        titulo = input("Qual o nome do filme? (0 para sair) ")

        if titulo == "0":
            break

        genero = input("Qual o gênero? ")
        duracao = int(input("Quanto tempo o filme tem em minutos? "))
        diretor = input("Quem é o diretor do filme? ")

        with open("filmes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{titulo}, {genero}, {duracao}, {diretor}\n")

        print("Filme adicionado com sucesso!\n")


def contar_filmes():
    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        quantidade = len(arquivo.readlines())

    print("Quantidade de filmes:", quantidade)


def info_por_titulo():
    titulo_busca = input("Digite o título do filme: ")
    encontrado = False

    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) == 4:
                titulo = dados[0].strip()
                genero = dados[1].strip()
                duracao = dados[2].strip()
                diretor = dados[3].strip()

                if titulo.lower() == titulo_busca.lower():
                    print("\nInformações do filme:")
                    print(f"Título: {titulo}")
                    print(f"Gênero: {genero}")
                    print(f"Duração: {duracao} minutos")
                    print(f"Diretor: {diretor}")

                    encontrado = True
                    break

    if not encontrado:
        print("Filme não encontrado.")


def filmes_por_diretor():
    diretor_busca = input("Digite o nome do diretor: ")
    encontrado = False

    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        print("\nFilmes encontrados:")

        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) == 4:
                titulo = dados[0].strip()
                diretor = dados[3].strip()

                if diretor.lower() == diretor_busca.lower():
                    print(f"- {titulo}")
                    encontrado = True

    if not encontrado:
        print("Nenhum filme encontrado.")


def filmes_por_genero():
    genero_busca = input("Digite o gênero do filme: ")
    encontrado = False

    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        print("\nFilmes encontrados:")

        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) == 4:
                titulo = dados[0].strip()
                genero = dados[1].strip()

                if genero.lower() == genero_busca.lower():
                    print(f"- {titulo}")
                    encontrado = True

    if not encontrado:
        print("Nenhum filme encontrado.")


def media_duracao():
    soma = 0
    quantidade = 0

    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")

            if len(dados) == 4:
                duracao = int(dados[2].strip())

                soma += duracao
                quantidade += 1

    if quantidade == 0:
        print("Nenhum filme cadastrado.")
    else:
        media = soma / quantidade
        print(f"Média de duração: {media:.2f} minutos")


if __name__ == "__main__":
    while True:
        menu()

        opc = input("Escolha uma opção: ").strip()

        if opc == "0":
            adicionar_filme()

        elif opc == "1":
            contar_filmes()

        elif opc == "2":
            info_por_titulo()

        elif opc == "3":
            filmes_por_diretor()

        elif opc == "4":
            filmes_por_genero()

        elif opc == "5":
            media_duracao()

        elif opc == "6":
            print("Saindo.")
            break

        else:
            print("Opção inválida, tente novamente.")