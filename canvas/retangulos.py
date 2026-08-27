from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_rectangle(
    50, 50, 150, 100,
    fill = 'blue',
    outline='black'
)

canvas.pack()
janela.mainloop()