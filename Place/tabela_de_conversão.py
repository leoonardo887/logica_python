import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("400x200+50+100")

label_valor = tk.Label(root, text="Valor:").grid(row=0, column=1, sticky="w", padx=5)
entry_valor = tk.Entry(root, width=19); entry_valor.grid(row=0, column=2, padx=5, pady=5)

label_moeda_entrada = tk.Label(root, text="Qual a moeda de entrada?").grid(row=3, column=1, sticky="w", padx=5)
moeda_entrada = ttk.Combobox(root, width=16, values=["Dólar", "Euro", "Kwanza"]); moeda_entrada.grid(row=3, column=2, sticky="w", padx=5)

label_moeda_saida = tk.Label(root, text="Para qual você quer converter?").grid(row=4, column=1, sticky="w", padx=5)
moeda_saida = ttk.Combobox(root, width=16, values=["Dólar", "Euro", "Kwanza"]); moeda_saida.grid(row=4, column=2, sticky="w", padx=5)

label_conversao = tk.Button(root, text="Converter", command=) #falta cálculo. 

botao = tk.Button(root, text="Sair", command=quit)          #botão de saída
botao.place(x=350, y=150)

root.mainloop()