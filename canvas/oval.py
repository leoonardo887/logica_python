from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_oval(50, 50, 150,150, fill='red')
canvas.create_oval(200, 200, 400, 250, fill='green')

canvas.pack()

janela.mainloop()