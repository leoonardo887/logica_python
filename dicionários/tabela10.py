estoque = {
    "Alface": 0.45,
    "Batata":1.20,
    "Tomate":2.30,
    "Feijão":1.50,
}

prod = input("Digite o produto que você queira: ")

if prod in estoque:
  preco = estoque[prod]
  print("custa",preco,"reais")
else:
  print("produto não encontrado")