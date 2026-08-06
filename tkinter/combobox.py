import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

def selecao_mudou(evento):
    label.config(text=f"{evento.widget.get() }selecionado!")

combobox = ttk.Combobox(root, values=["Primeiro", "Segundo", "Terceiro"])
combobox.set("Primeiro")
combobox.bind("<<ComboboxSelect>>", selecao_mudou)
combobox.pack()

label = tk.Label(root, text="Primeiro Selecionado!")
label.pack

root.mainloop()

#é uma caixa de seleção, onde o usuário pode escolher uma opção dentre várias.