#faz a média dos alunos dentro do dicionário
sala = {}
n = int(input("Quantos alunos há na turma? "))
for i in range(n):
  nome = input("qual o nome do aluno? ")
  nota = float(input("qual a nota? "))
  sala[nome] = nota

for nome,nota in sala.items():
  print(f'\n Aluno: {nome} - Nota: {nota}')
  media = sum(sala.values()) / len(sala)
print("\n a média é",media)