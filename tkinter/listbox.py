import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        idx = sel[0]
        label.config(text=f"{evento.widget.get(idx)} Selecionado!")

listbox = tk.Listbox(root)
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", selecao_mudou)
listbox.pack(expand=True)

label = tk.Label(root, text="Primeiro selecionado!")
label.pack()

root.mainloop()

#criado para criar uma lista de opções, onde o usuário pode selecionar uma opção dentre várias.