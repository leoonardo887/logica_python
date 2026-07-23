# Função que mostra as opções disponíveis para o usuário
def menu():
    print("\n0 - Adicionar filme")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


# Função responsável por adicionar filmes no arquivo
def adicionar_filme():

    # Mantém o cadastro funcionando até o usuário escolher sair
    while True:

        # Pede o título do filme
        # Digitar "0" encerra o cadastro
        titulo = input("Qual o nome do filme? (0 para sair) ")

        # Verifica se o usuário quer sair
        if titulo == "0":
            break

        # Recebe as outras informações do filme
        genero = input("Qual o gênero? ")

        # Converte a duração digitada para número inteiro
        duracao = int(input("Quanto tempo o filme tem em minutos? "))

        diretor = input("Quem é o diretor do filme? ")

        # Abre o arquivo no modo "a" (adicionar)
        # Assim os filmes antigos não são apagados
        with open("filmes.txt", "a", encoding="utf-8") as arquivo:

            # Salva os dados do filme separados por vírgula
            arquivo.write(f"{titulo}, {genero}, {duracao}, {diretor}\n")

        print("Filme adicionado com sucesso!\n")


# Função que conta quantos filmes existem no arquivo
def contar_filmes():

    # Abre o arquivo para leitura
    with open("filmes.txt", "r", encoding="utf-8") as arquivo:

        # Lê todas as linhas e conta a quantidade delas
        # Cada linha representa um filme
        quantidade = len(arquivo.readlines())

    # Mostra a quantidade encontrada
    print("Quantidade de filmes:", quantidade)


# Função que busca informações de um filme pelo título
def info_por_titulo():

    # Pede o título que será pesquisado
    titulo_busca = input("Digite o título do filme: ")

    # Variável usada para saber se encontrou o filme
    encontrado = False

    # Abre o arquivo para leitura
    with open("filmes.txt", "r", encoding="utf-8") as arquivo:

        # Lê cada filme do arquivo
        for linha in arquivo:

            # Remove espaços e separa os dados pela vírgula
            dados = linha.strip().split(",")

            # Confere se a linha possui as 4 informações esperadas
            if len(dados) == 4:

                # Guarda cada informação em uma variável
                titulo = dados[0].strip()
                genero = dados[1].strip()
                duracao = dados[2].strip()
                diretor = dados[3].strip()

                # Compara os títulos ignorando letras maiúsculas e minúsculas
                if titulo.lower() == titulo_busca.lower():

                    # Mostra os dados do filme encontrado
                    print("\nInformações do filme:")
                    print(f"Título: {titulo}")
                    print(f"Gênero: {genero}")
                    print(f"Duração: {duracao} minutos")
                    print(f"Diretor: {diretor}")

                    # Marca que encontrou o filme
                    encontrado = True

                    # Para a busca
                    break

    # Caso não tenha encontrado nenhum filme
    if not encontrado:
        print("Filme não encontrado.")


# Função que procura filmes pelo nome do diretor
def filmes_por_diretor():

    # Pede o nome do diretor
    diretor_busca = input("Digite o nome do diretor: ")

    encontrado = False

    # Abre o arquivo para leitura
    with open("filmes.txt", "r", encoding="utf-8") as arquivo:

        print("\nFilmes encontrados:")

        # Procura em cada linha do arquivo
        for linha in arquivo:

            # Separa as informações do filme
            dados = linha.strip().split(",")

            if len(dados) == 4:

                # Pega o título e o diretor
                titulo = dados[0].strip()
                diretor = dados[3].strip()

                # Compara o diretor pesquisado com o diretor salvo
                if diretor.lower() == diretor_busca.lower():

                    # Mostra o filme encontrado
                    print(f"- {titulo}")
                    encontrado = True

    # Caso nenhum filme seja encontrado
    if not encontrado:
        print("Nenhum filme encontrado.")


# Função que procura filmes pelo gênero
def filmes_por_genero():

    # Pede o gênero que será pesquisado
    genero_busca = input("Digite o gênero do filme: ")

    encontrado = False

    # Abre o arquivo para leitura
    with open("filmes.txt", "r", encoding="utf-8") as arquivo:

        print("\nFilmes encontrados:")

        # Percorre todos os filmes
        for linha in arquivo:

            # Divide os dados do filme
            dados = linha.strip().split(",")

            if len(dados) == 4:

                # Pega o título e o gênero
                titulo = dados[0].strip()
                genero = dados[1].strip()

                # Verifica se o gênero é igual ao pesquisado
                if genero.lower() == genero_busca.lower():

                    # Mostra o filme encontrado
                    print(f"- {titulo}")
                    encontrado = True

    # Caso não encontre nenhum filme
    if not encontrado:
        print("Nenhum filme encontrado.")


# Função que calcula a média de duração dos filmes
def media_duracao():

    # Guarda a soma de todas as durações
    soma = 0

    # Conta quantos filmes existem
    quantidade = 0

    # Abre o arquivo para leitura
    with open("filmes.txt", "r", encoding="utf-8") as arquivo:

        # Lê todos os filmes
        for linha in arquivo:

            # Separa as informações
            dados = linha.strip().split(",")

            if len(dados) == 4:

                # Transforma a duração em número inteiro
                duracao = int(dados[2].strip())

                # Soma a duração
                soma += duracao

                # Aumenta a quantidade de filmes
                quantidade += 1

    # Verifica se existe algum filme cadastrado
    if quantidade == 0:
        print("Nenhum filme cadastrado.")

    else:

        # Calcula a média
        media = soma / quantidade

        # .2f mostra somente 2 casas depois da vírgula
        print(f"Média de duração: {media:.2f} minutos")


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":

    # Repete o menu até o usuário escolher sair
    while True:

        # Mostra o menu na tela
        menu()

        # Recebe a opção escolhida pelo usuário
        opc = input("Escolha uma opção: ").strip()

        # Chama a função correspondente à escolha
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

        # Encerra o programa
        elif opc == "6":
            print("Saindo.")
            break

        # Caso o usuário digite uma opção inexistente
        else:
            print("Opção inválida, tente novamente.")