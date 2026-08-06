import tkinter as tk

root = tk.Tk()
root.title=("SENAI - Desenvolvimento de Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

root.mainloop()

#faz um fundo cor azul claro na janela, com largura e altura de 200px, e uma distância de 10px entre a borda da janela e o frame.