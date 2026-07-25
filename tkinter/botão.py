import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def button_command():
    messagebox.showinfo(
        "Informação",
        "Você clicou no botão!"
    )

button = tk.Button(
    root,
    text="Clique aqui!",
    command=button_command
)
button.pack()

root.mainloop()