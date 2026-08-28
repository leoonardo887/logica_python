from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas= Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_text(200, 150, text="Seu texto", font= ('Arial', 20), fill='black')

canvas.pack()

janela.mainloop()

#arial é o tamanho da fonte