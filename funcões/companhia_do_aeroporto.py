viagens = {}

def menu():
    print("\n0 - Adicionar viagem que queira fazer")
    print("1 - Quantidade total de viagens")
    print("2 - Visualizar viagens")
    print("3 - Sair")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        destino = input("Digite o destino da viagem. ")
        horario = int(input("Digite o horário da viagem. "))
        viagens[destino] = horario

    elif opcao == 1:
        print(f"Quantidade total de viagens: {len(viagens)}")

    elif opcao == 2:
        for destino, horario in viagens.items():
            print(f"Destino: {destino}, Horário: {horario}")
    else:
        break