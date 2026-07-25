import tkinter as tk

janela_largura = 300
janela_altura = 200

root = tk.Tk()

tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

centro_x = int(tela_largura / 2 - janela_largura / 2)
centro_y = int(tela_altura / 2 - janela_altura / 2)

root.geometry(f'{janela_largura}x{janela_altura}+{centro_x}+{centro_y}')

root.resizable(False, False)
#Não possibilita mudar o tamanho da janela.

root.attributes('-alpha', 0.5)
#isso altera a opacidade da janela.

root.mainloop()