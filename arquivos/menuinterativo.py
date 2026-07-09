def menu():
    print("0 - Para adicionar filme(adicional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - média de duração dos filmes")
    print("6 - sair")
    interacao = int(input("O que você deseja? "))

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
        elif opc == "4"
            filmes_por_genero()
        elif opc == "5":
            media_duracao()
        elif opc == "6":
            print("Saindo. ")
            break
        else:
            print("Opção inválida, tente novamente. ")