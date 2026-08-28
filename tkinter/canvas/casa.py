from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_rectangle(
    250, 200, 100, 100,
    fill = 'brown',
    outline='black'
)

canvas.create_rectangle(
    200, 145, 155, 200,
    fill = 'red',
    outline='black'
)

canvas.create_polygon(
    175,25,
    250,100,
    100,100,
    fill='brown',
    outline="black"
)

canvas.create_rectangle(
    120, 150, 140, 170,
    fill = 'yellow',
    outline='black'
)

canvas.create_rectangle(
    230, 150, 210, 170,
    fill = 'yellow',
    outline='black'
)

canvas.pack()

janela.mainloop()