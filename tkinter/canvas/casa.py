from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="light blue")

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

canvas.create_polygon(
    0,300,
    0,200,
    500,200,
    500,300,
    fill='green',
    outline="black"
)

#carcaça do carro
canvas.create_polygon(
    350,160,
    300,160,
    280,180,
    260,190,
    370,190,
    fill='blue',
    outline="black"
)

#rodas
canvas.create_oval(305, 200, 280,185, fill='black')

canvas.create_oval(355, 200, 330,185, fill='black')

canvas.pack()

janela.mainloop()