def linhas():
    # Cria uma linha horizontal usando o tamanho definido na variável largura
    # Exemplo: +----------------------------------------+
    print(f"+{largura*'-'}+")


def colunas():
    # Cria as linhas verticais do menu e coloca a palavra no centro
    for linha in range(altura):
        # Verifica se chegou na linha do meio para colocar o texto centralizado
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            # Cria uma linha vazia dentro das colunas
            print(f"|{largura*' '}|")


def adicionar_filme():
    # Função responsável por adicionar filmes no arquivo Arq_Filmes.txt
    while True:

        # Pede o título do filme ao usuário
        # Digitar "Pare" encerra o cadastro
        titulo = input("Escreva o título do filme: (Digite *Pare* para sair)")

        # Se o usuário digitar Pare, sai do while
        if titulo == "Pare":
            break

        # Recebe as outras informações do filme
        diretor = input("Escreva o nome do diretor: ")
        genero = input("Escreva o gênero do filme: ")
        tempo = input("Escreva quantos minutos de duração tem o filme: ")

        # Abre o arquivo no modo "a" (append), adicionando sem apagar os dados existentes
        with open("Arq_Filmes.txt", "a", encoding="utf-8") as f:
            # Escreve as informações do filme separadas por " - "
            f.write(f"{titulo} - {diretor} - {genero} - {tempo}\n")

    # Mensagem exibida quando termina a função
    print("Filme adicionado com sucesso!")


def quantidade_de_filmes():
    # Abre o arquivo para leitura
    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:

        # Conta quantas linhas existem no arquivo
        # Cada linha representa um filme cadastrado
        quantidade = len(f.readlines())

        # Mostra a quantidade de filmes
        print(f"Quantidade de filmes: {quantidade}")


def informacao_filme():
    # Pede o título do filme que será pesquisado
    titulo_procurado = input("Digite o titulo do filme: ")

    # Abre o arquivo para leitura
    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:

        # Variável usada para saber se encontrou o filme
        encontrado = False

        # Percorre cada linha do arquivo
        for linha in f:

            # Remove espaços e separa as informações pelo " - "
            dados = linha.strip().split(" - ")

            # Compara os títulos ignorando letras maiúsculas e minúsculas
            if dados[0].lower() == titulo_procurado.lower():

                # Mostra as informações do filme encontrado
                print(f"Título: {dados[0]}")
                print(f"Diretor: {dados[1]}")
                print(f"Gênero: {dados[2]}")
                print(f"Duração: {dados[3]} minutos")

                # Marca que encontrou e encerra a busca
                encontrado = True
                break

        # Caso nenhum filme seja encontrado
        if not encontrado:
            print("Filme não encontrado.")


def diretor_filme():
    # Pede o nome do diretor para pesquisar
    diretor_procurado = input("Digite o diretor do filme: ")

    # Abre o arquivo para leitura
    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:

        # Controla se algum filme foi encontrado
        encontrado = False

        # Percorre todos os filmes
        for linha in f:
            dados = linha.strip().split(" - ")

            # Verifica se o diretor é igual ao pesquisado
            if dados[1].lower() == diretor_procurado.lower():

                # Mostra o título do filme
                print(f"Título: {dados[0]}")
                encontrado = True

        # Caso não encontre nenhum filme
        if not encontrado:
            print("Nenhum filme encontrado no nome desse diretor.")


def genero_filme():
    # Pede o gênero que será pesquisado
    genero_procurado = input("Digite o gênero do filme: ")

    # Abre o arquivo para leitura
    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:

        encontrado = False

        # Percorre todos os filmes do arquivo
        for linha in f:
            dados = linha.strip().split(" - ")

            # Compara o gênero do arquivo com o gênero pesquisado
            if dados[2].lower() == genero_procurado.lower():

                # Mostra o título dos filmes encontrados
                print(f"Título: {dados[0]}")
                encontrado = True

        # Caso não encontre filmes desse gênero
        if not encontrado:
            print("Nenhum filme encontrado com esse gênero.")


def media_filmes():
    # Guarda a soma de todas as durações
    soma_duracao = 0

    # Conta quantos filmes existem
    quantidade = 0

    # Abre o arquivo para leitura
    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:

        # Percorre cada filme
        for linha in f:

            # Divide as informações do filme
            dados = linha.strip().split(" - ")

            # Transforma a duração em número inteiro
            duracao = int(dados[3])

            # Soma a duração do filme
            soma_duracao += duracao

            # Aumenta a quantidade de filmes
            quantidade += 1

        # Verifica se existem filmes cadastrados
        if quantidade > 0:

            # Calcula a média de duração
            media = soma_duracao / quantidade

            # .2f mostra apenas 2 números depois da vírgula
            print(f"A média de duração dos filmes é de {media:.2f} minutos.")

        else:
            print("Não existem filmes arquivados.")


# Define a altura do menu
altura = 1

# Define a largura da caixa do menu
largura = 39

# Lista com todas as opções do menu
palavras = (
    "Adicionar Filme - 0",
    "Quantidade total de filmes - 1",
    "Informações de um filme pelo titulo - 2",
    "Filmes de um diretor específico - 3",
    "Filmes de um gênero específico - 4",
    "Média de duração dos filmes - 5",
    "Sair - 6"
)


if __name__ == "__main__":
    # Executa esse bloco somente se o arquivo for aberto diretamente

    # Cria o menu desenhado na tela
    for palavra in palavras:
        linhas()
        colunas()

    # Cria a última linha do menu
    linhas()


# Loop principal do programa
# Mantém o menu funcionando até o usuário escolher sair
while True:

    # Recebe a escolha do usuário
    opcao = input("O que você deseja fazer: ")

    # Chama a função correspondente à opção escolhida
    if opcao == "0":
        adicionar_filme()

    elif opcao == "1":
        quantidade_de_filmes()

    elif opcao == "2":
        informacao_filme()

    elif opcao == "3":
        diretor_filme()

    elif opcao == "4":
        genero_filme()

    elif opcao == "5":
        media_filmes()

    # Encerra o programa
    elif opcao == "6":
        break

    # Verifica se o número é maior que as opções disponíveis
    elif opcao > "6":
        print("Número maior que o desejado. (0-6)")

    # Verifica se o número é menor que as opções disponíveis
    elif opcao < "0":
        print("Número menor que o desejado. (0-6)")