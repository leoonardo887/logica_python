nomes = ["Ana", "Bruno", "Carlos"]
with open("nomes.txt", "w") as f:
    for nome in nomes:
        f.write(nome + "\n")