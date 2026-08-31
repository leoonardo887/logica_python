from tkinter import Tk, Canvas
from tkinter import ttk

janela = Tk()
janela.geometry("400x300")

#cores.
cor0 = "#000000"  # Preto
cor1 = "#8B4513"  # Marrom
cor2 = "#FF0000"  # Vermelho
cor3 = "#FFA500"  # Laranja
cor4 = "#FFFF00"  # Amarelo
cor5 = "#008000"  # Verde
cor6 = "#0000FF"  # Azul
cor7 = "#800080"  # Violeta
cor8 = "#808080"  # Cinza
cor9 = "#FFFFFF"  # Branco

cor_dourado = "#FFD700"   # Dourado
cor_prateado = "#C0C0C0"  # Prateado

primeira_cor = ttk.Combobox(janela, values=["Primeiro", "Segundo", "Terceiro"])
primeira_cor["values"] = ["Preto", "Marrom", "Vermelho", "Laranja","Amarelo","Verde","Azul","Violeta","Cinza","Branco"]
primeira_cor.pack(padx=300,pady=200)

canvas = Canvas(janela, width=400, height=200, bg="light blue") #selecionar posição do desenho do resistor

canvas.pack()
janela.mainloop()