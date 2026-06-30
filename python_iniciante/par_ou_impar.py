x = 1
while x <=20:
  if x % 2 ==0:
    print(f'{x} - Número par')
  else:
    print(f'{x} - Número impar')
  x = x + 1
# %(módulo) quer dizer que um numero dividido pelo número depois do módulo em que o resto dê o número que está após o ==
#no exemplo acima, o módulo indica que se x for divisivel por 2 e o resto dê 0, o número é par, se não, impar.