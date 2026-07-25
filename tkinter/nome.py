import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

def button_command():
    nome = entry.get()
    messagebox.showinfo("Nome completo", nome)

label = tk.Label(root, text="Digite seu nome completo: ")
entry = tk.Entry(root)
button = tk.Button(root, text="Mostrar", command=button_command)

label.pack()
entry.pack()
button.pack()

root.mainloop()