import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

minha_imagem = tk.PhotoImage(file="pikachu.png")

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)

root.mainloop()

#Tem que ter a imagem baixada antes de executar o arquivo