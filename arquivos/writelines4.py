filmes = {
    "Título: O Poderoso Chefão",
    "Ano: 1972",
    "Diretor: Francis Ford Coppola",
    "Gênero: Crime, drama",
    "Duração: 175 minutos",

    "Título: Interestelar",
    "Ano: 2014",
    "Diretor: Christopher Nolan",
    "Gênero: Ficção Científica, Aventura",
    "Duração: 169 minutos",

    "Título: 2001 - Uma Odisseia No Espaço",
    "Ano: 1968",
    "Diretor: Stanley Kubrick",
    "Gênero: Ficção científica",
    "Duração: 142 minutos"
        }
with open("filmes.txt", "w") as f:
    for filme in filmes:
        f.write(filme + "\n" )