#sempre que queira passar alguma variável para uma função, você precisa colocar ela dentro dos parênteses da função.
def saudacao(nome):
    print(f"oii, {nome}")

nome = "Leonardo"
# Não faça assim quando a função não retorna algum valor.
# print(saudacao(nome))

#faça assim
saudacao(nome)