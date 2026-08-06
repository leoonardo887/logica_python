import tkinter as tk

root = tk.Tk()
root.title=("SENAI - Desenvolvimento de Sistemas")
root.geometry("500x300")
root.config(bg="skyblue")   # bg significa back ground, fundo

frame = tk.Frame(root, width=2000, height=2000, bg="yellow")
frame.pack(padx=10, pady=10)

nested_frame = tk.Frame(frame, width=100, height=100, bg="red")     # Cria um frame dentro de outro frame, porque se usa frame invés de root. 
nested_frame.pack(padx=10, pady=10)

root.mainloop()