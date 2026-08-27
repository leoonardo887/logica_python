from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_line(
    10,10,10,200,         #os dois primeiros 10 são o ponto onde começa a linha
    fill='black',          #e os dois 200 são os pontos onde termina a linha
    width=3
)

canvas.create_line(
    10,10,200,10,         #os dois primeiros 10 são o ponto onde começa a linha
    fill='black',          #e os dois 200 são os pontos onde termina a linha
    width=3
)

canvas.pack()

janela.mainloop()