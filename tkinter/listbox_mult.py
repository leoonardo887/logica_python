import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")

def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        itens = [evento.widget.get(i) for i in sel]
        label.config(text=f"{', '.join(itens) } selecionado(s)! ")
    else:
        label.config(text="Nenhum item selecionado")

listbox = tk.Listbox(root, selectmode="multiple")
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", selecao_mudou)
listbox.pack(expand=True)

label = tk.Label(root, text="Primeiro selecionado!")
label.pack()

root.mainloop()

#criado para criar uma lista de opções, onde o usuário pode selecionar uma ou mais opções dentre várias.