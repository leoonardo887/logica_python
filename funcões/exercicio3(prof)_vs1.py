altura = int(input("qual a altura do quadrilatero? "))
largura = int(input("qual a largura do quadrilatero? "))


print("+", end="")
for c in range(largura):
    print('-',end="")
print("+")

for l in range(altura):
    print("|", end="")
    for c in range(largura):
        print(" ", end="")
    print("|")

print("+", end="")
for c in range(largura):
    print('-',end="")
print("+")