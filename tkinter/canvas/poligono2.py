#pentagono

from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="black")

canvas.create_polygon(
    50,60,
    100,10,
    150,60,
    125,110,
    75,110,
    fill='white',
)

canvas.pack()

janela.mainloop()