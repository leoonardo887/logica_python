import tkinter as tk

#cria a janela principal
root = tk.Tk()

#cria um rótulo (label) com o texto "hello world"
message = tk.Label(root, text="Hello, world!")

#posiciona o rótulo na janela
message.pack()

#Define o tamanho da janela (largura x altura + posição eixo x + posição eixo y)
root.geometry("400x200+50+250")

#inicia o loop principal da interface gráfica
root.mainloop()