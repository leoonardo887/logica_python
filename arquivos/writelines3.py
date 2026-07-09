nomes = []

for i in range(3):
    nome = input("Digite um nome. ")
    nomes.append(nome)

with open("nomes2.txt", "w")as f:               #cria um arquivo com os nomes que digitaste. 
    for nome in nomes:
        f.write(nome + "\n")

