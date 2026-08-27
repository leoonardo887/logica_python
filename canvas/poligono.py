from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_polygon(
    100,50,
    150,150,
    50,150,
    fill='green',
)

canvas.pack()

janela.mainloop()