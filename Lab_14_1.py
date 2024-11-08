import matplotlib.pyplot as plt  
import numpy as np

x = np.linspace(1, 10, 100)  

y = x ** np.sin(10 * x)

plt.plot(x, y, label=r'$x^{\sin(10x)}$', color="green", linewidth=2)

plt.title('Graph of Y(x) = x^sin(10x)', fontsize=15)  # назва графіка
plt.xlabel('x', fontsize=12, color='blue')  # позначення вісі абсцис
plt.ylabel('Y(x)', fontsize=12, color='blue')  # позначення вісі ординат
plt.legend()
plt.grid(True)
plt.show()
