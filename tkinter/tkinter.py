import tkinter as tk

#cria a janela principal
root = tk.Tk()

#cria um rótulo (label) com o texto "hello world"
message = tk.Label(root, text="Hello, world!")

#posiciona o rótulo na janela
message.pack()

#inicia o loop principal da interface gráfica
root.mainloop()