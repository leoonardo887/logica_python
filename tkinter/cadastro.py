import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")


minha_imagem = tk.PhotoImage(file="mcqueen.png")

label = tk.Label(root, image=minha_imagem)
label.pack(side="left")
#Tem que ter a imagem baixada antes de executar o arquivo 

#O código vai aqui!!

root.mainloop()