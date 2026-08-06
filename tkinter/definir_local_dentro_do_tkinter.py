import tkinter as tk

root = tk.Tk()
root.title=("SENAI - Desenvolvimento de Sistemas")
root.geometry("340x100")

tk.Button(root, text="Top Button!").pack()
tk.Label(root, text="Hello, Left!").pack(side="left")
tk.Label(root, text="Hello, Right!").pack(side="right")
tk.Checkbutton(root, text="Uma opção na parte inferior!").pack(side=tk.BOTTOM)

root.mainloop()

#criado para definir a posição dos elementos na tela, utilizando o pack.