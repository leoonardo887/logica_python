import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x100")

def button_command():
    messagebox.showinfo(
        "Informação",
        "Você clicou no botão!"
    )

def button_command2():
    messagebox.showinfo(
        "Informação",
        "Você clicou no segundo botão!"
    )


button = tk.Button(
    root,
    text="primeiro botão.",
    command=button_command
)

button2 = tk.Button(
    root,
    text="segundo botão.",
    command=button_command2
)

button.pack()                       #código que poe a função criada dentro da janela. 
button2.pack()
root.mainloop()