n = int(input("de qual número você quer a tabuada? "))
y = 1      #y = 1 quer dizer que ele começa valendo 1, y é quem vai multiplicar, 1, 2, 3, ... até 10.
while y<=10:          #enquanto y menor que dez...
  print(f'{n} x {y} = {n*y}')         #printe n vezes y
  y += 1