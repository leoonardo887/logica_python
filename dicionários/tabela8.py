filme = {
    "titulo":"Star Wars",
    "ano":1977,
    "diretor":"George Lucas"
}                                 #value equivale ao que tá dentro das casas (zero,um,...)
for k,v in filme.items():         #keys equivale ao primeiro valor (casa zero, um, ...)
  print(f'O {k} é {v}')           #.items equivale a todos os valores dentro da aspa.