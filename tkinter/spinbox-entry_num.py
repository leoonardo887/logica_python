import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

#StringVar é uma variavel que armazena uma string
#é usada para atualizar widget dinamicamente
spinbox_var = tk.StringVar(value="0")

spinbox = tk.Spinbox(root,
                     from_=10,
                     to=10,
                     #  incremet=5,
                     textvariable=spinbox_var)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable=spinbox_var)
label.pack()

root.mainloop()

#é uma caixa de seleção, onde o usuário pode escolher um número dentre vários, e o valor selecionado é exibido em um label.