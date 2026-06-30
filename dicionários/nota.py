sala = {}
n = int(input("Digite o número de alunos de uma turma: "))        #precisa ser int pq não se pode repetir alguma coisa x,y vezes.

for i in range(n):
  nome = input("qual o nome do aluno? ")
  nota = input("qual a nota? ")
  sala[nome] = nota

for nome,nota in sala.items():
  print(f'\n Aluno: {nome} - Nota: {nota}')