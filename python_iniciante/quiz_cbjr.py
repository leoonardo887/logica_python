print('quiz sobre Charlie Brown jr')
pontos = 0
resposta = input("o vocalista da banda cbjr, Chorão, morreu em que ano? ((a)2013/(b)2014/(c)2015/(d)2012): ")
if resposta == "a":
  pontos = pontos + 1
resposta_dois = input("qual a música mais ouvida da banda? ((a)Céu Azul/(b)Me Encontra/(c)Dias de Luta, Dias de Glória/(d)Só os Loucos Sabem): ")
if resposta_dois == "c":
  pontos = pontos + 1
resposta_tres = input("a frase {-eu procurei em outros olhos enxergar você-} é letra de qual música? ((a)Quebra Mar/(b)Como Tudo Deve Ser/(c)Só Por Uma Noite/(d)I Feel So Good Today): ")
if resposta_tres == "c":
  pontos = pontos + 1
print("pontuação:",pontos)
if pontos == 3:
  print("Parabéns você gabaritou!!")
elif pontos == 2:
  print("Parabéns, não foi tão mal")
elif pontos == 1:
  print("leia o livro da Graziela Gonçalves por favor")
else:
  print("VÁ ESCUTAR CHARLIE BROWN")
input("para finalizar, qual sua música favorita da banda?? ")
print('ótimo gosto!!')