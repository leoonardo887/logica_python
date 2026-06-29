#verificar idade para dirigir usando if e else corretamente
idade = int(input("Qual sua idade? "))
habilitacao = input("você tem habilitação para dirigir? ")

pode_dirigir = idade >= 18 and habilitacao == 'sim'

if pode_dirigir:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")