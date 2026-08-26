x = int(input("Digite um número inicial. "))
y = int(input("Digite um número final. "))

while x <= y:
    if x % 2 == 0:
        print(x)
    x += 1
