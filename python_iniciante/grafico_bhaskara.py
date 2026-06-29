import matplotlib.pyplot as plt
import numpy as np

# 1. Definir os coeficientes da equação ax^2 + bx + c
a = int(input("Qual número acompanha x^2? "))
b = int(input("Qual número multiplica x? "))
c = int(input("Qual o termo independente? "))

# 2. Gerar valores de x (domínio) e calcular y
x = np.linspace(-5, 15, 100) # 100 pontos entre -10 e 10
y = a*x**2 + b*x + c

# 3. Criar o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f'{a}x² + {b}x + {c}')

# 4. Adicionar detalhes
plt.title('Gráfico da Equação do Segundo Grau')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=1) # Eixo x
plt.axvline(0, color='black',linewidth=1) # Eixo y
plt.grid(True)
plt.legend()

# 5. Exibir
plt.show()