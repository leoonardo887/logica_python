import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="black")            #define a cor de fundo da janela.

frame = tk.Frame(root, width=420, height=220)       #define a largura e altura do bloco de cor.
frame.pack(padx=10, pady=10)            #define a distância entre a borda da janela e o bloco de cor. 

a_frame = tk.Frame(frame, width=190, height=190, bg="red")
a_frame.pack(side="top", padx=10, pady=10)

b_frame = tk.Frame(frame, width=190, height=190, bg="yellow")
b_frame.pack(padx=10, pady=10)

c_frame = tk.Frame(frame, width=190, height=190, bg="green")
c_frame.pack(side="bottom", padx=10, pady=10)

root.mainloop()

