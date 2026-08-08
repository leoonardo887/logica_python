import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

for linha in range(3):
    for coluna in range(3):
        tk.Button(
            root,
            text=f"Cell ({linha}, {coluna})",
            width=20,
            height=5
        ).grid(row=linha, column=coluna, padx=2, pady=2)

tk.button(
    root,
    text="Span 2 columns",
    height=5
).grid(row=3, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

tk.Button(
    root,
    text="Span 2 rows",
    width=20,
    height=10
).grid(row=0, column=3, rowspan=2, sticky="ns", padx=2, pady=2)

#grid é a localização do elemento dentro da janela, onde pode dividi-la em várias partes, e dividir tudo por linhas. 

root.mainloop()