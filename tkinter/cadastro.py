import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk

root = tk.Tk()
root.title("SENAI - Sistemas")

def mostrar_nome():
    messagebox.showinfo('titulo',f"Seu nome é {entry_nome.get()}")

minha_imagem = tk.PhotoImage(file="perfil sem imagem.png").subsample(3, 3)  

#diminui o tamanho da imagem pela metade
label_imagem = tk.Label(root, image=minha_imagem)
label_imagem.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
# rowspan=6 faz a imagem ocupar 6 linhas, e não apenas uma.

label_nome = tk.Label(root, text="Nome:").grid(row=0, column=1, sticky="w", padx=5)
entry_nome = tk.Entry(root, width=25); entry_nome.grid(row=0, column=2, padx=5, pady=5)

label_gen = tk.Label(root, text="Gênero:").grid(row=1, column=1, sticky="w", padx=5)
combo_gen = ttk.Combobox(root, values=["Masculino", "Feminino"], width=22); combo_gen.grid(row=1, column=2, padx=5, pady=5)

label_cor = tk.Label(root, text="Cor dos olhos:").grid(row=2, column=1, sticky="w", padx=5)
combo_cor = ttk.Combobox(root, values=["Azul", "Verde", "Castanho"], width=22); combo_cor.grid(row=2, column=2, padx=5, pady=5)

label_alt = tk.Label(root, text="Altura(cm):").grid(row=3, column=1, sticky="w", padx=5)
entry_alt = tk.Entry(root, width=25); entry_alt.grid(row=3, column=2, padx=5, pady=5)

label_peso = tk.Label(root, text="Peso(Kg):").grid(row=4, column=1, sticky="w", padx=5)
entry_peso = tk.Entry(root, width=25); entry_peso.grid(row=4, column=2, padx=5, pady=5)

botao = tk.Button(root, text="Enviar",command=mostrar_nome, width=10, height=1)
botao.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()

#O CÓDIGO FUNCIONA CORRETAMENTE APENAS SE TIVER A IMAGEM BAIXADA. 

#o sticky (na linha dos labels) define onde o texto fica dentro da célula da tabela, o texto pode ficar no centro, na direita ou na esquerda.

#"w" = West (Oeste) = esquerda
#"e" = East = direita
#"n" = North = cima
#"s" = South = baixo