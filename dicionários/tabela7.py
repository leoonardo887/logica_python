banca = {
    "Diário": [25, 6.7],
    "Mangá": [20, 20.00],
    "Jornal": [15, 10.00]
}
qtd = banca ["Diário"] [0]
preco = banca["Diário"][1]
for chave, valor in banca.items():
  print(chave, "tem", valor[0],"itens no estoque, e o preço de cada um é", valor[1])