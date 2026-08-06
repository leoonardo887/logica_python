import tkinter as tk
from tkinter import ttk

root = tk.Tk()  # A janela principal, a raiz o root.
root.title("SENAI - Desenvolvimento de Sistemas")   # Título que estará acima da janela
root.geometry("300x200")    # Tamanho da janela

def calculo():
    """Faz o cálculo do IMC"""
    try:    # Try é usado quando o código pode dar um erro, então após ele é usado um except.
        peso = float(entrypeso.get().replace(",", "."))   # O .get pegao que foi digitado em uma caixa entry e envia para o sistema.
        altura = float(entryaltura.get().replace(",", "."))   # Nesse caso o .get envia os números para que o IMC possa ser calculado.
        # .replace substitui o primeiro " ",que seria a vírgula, pelo segundo (ponto) para evitar erros como no caso do usuario usando , ao invés de . em sistemas em python.
        #ou seja ele troca a vírgula digitada pelo usuário, por ponto para o python reconhecer. 

        imc = peso / (altura*altura)    # Não se pode digitar palavras pois elas resultariam num erro no cálculo.

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        resultado.config(   # O .config é usado para alterar a proptiedade de um widget, nesse caso ele muda o label resultado que era "" para "Seu IMC é: {imc:.2f}\nClassificação: {classificacao}".
            text=f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}"    # \n passa o resto do texto para linha de baixo.
        )
        labelinstrucao.config(
            text=""
        )

    except ValueError:  # Except é usado quando o código da erro, então ele comanda o sistema fazer outra coisa ao invés de ser interrompido, nesse caso impimir uma mensagem.
        resultado.config(text="Digite valores válidos!")


labelpeso = tk.Label(root, text="Peso(Kg)")     #tk.Label são as palavras que aparecerão na interface gráfica.
labelpeso.pack()    # .pack() manda a variavel para a interface
entrypeso = tk.Entry(root)  # Entry é usado no Tkinter para que o usuario possa digitar uma linha de texto
entrypeso.pack()

labelaltura = tk.Label(root, text="Altura(m)")
labelaltura.pack()
entryaltura = tk.Entry(root)
entryaltura.pack()

button = tk.Button(     #tk.Button cria um botão na interface que faz alguma coisa quando clicado.    
    root,               # É onde o botão está, nesse caso a janela principal, a raiz o root.
    text="Calcular",    # O texto que estará em cima do botão
    command=calculo     # O comando que ele vai fazer
    )
button.pack()

labelinstrucao = tk.Label(root, text="Preencha os campos e clique em calcular.")
labelinstrucao.pack()

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()