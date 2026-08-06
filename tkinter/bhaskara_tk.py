import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Praticando")
root.geometry("800x600")

def baskhara():
    try:
        A = float(entryA.get())

        if A == 0:
            resultado.config(text="O valor A não pode ser igual a 0.")
            return
        B = float(entryB.get())
        C = float(entryC.get())

        delta = B**2-4*A*C
        if delta < 0:
            resultado.config(text="A equação não possui raizes reais.")
            return
        raizdelta = delta **0.5
        
        baskhara1 = (-B + raizdelta) / (2*A)
        baskhara2 = (-B - raizdelta) / (2*A)

        resultado.config(
            text=f'Os resultados são {baskhara1} e(ou) {baskhara2}'
        )
    except ValueError:
        resultado.config(text="Digite valores válidos.")



labelA = tk.Label(root, text="Número A:")
labelA.pack()
entryA = tk.Entry(root)
entryA.pack()

labelB = tk.Label(root, text="Número B:")
labelB.pack()
entryB = tk.Entry(root)
entryB.pack()

labelC = tk.Label(root, text="Número C:")
labelC.pack()
entryC = tk.Entry(root)
entryC.pack()

botao = tk.Button(
    root,
    text="Calcular",
    command=baskhara
)
botao.pack()

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()