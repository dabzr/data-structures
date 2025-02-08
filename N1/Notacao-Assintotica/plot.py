import matplotlib.pyplot as plt
import numpy as np
 
lim = 10000
n = np.arange(1, lim, lim/20)
 
O1 = np.ones_like(n)
On = n
On2 = n**2
Ologn = np.log(n)
Onlogn = n*np.log(n)
 
plt.plot(n, O1, label="O1", marker='o')
plt.plot(n, On2, label="On2", marker='^')
plt.plot(n, On, label="On", marker='s')
plt.plot(n, Ologn, label="Ologn", marker='x')
plt.plot(n, Onlogn, label="Onlogn", marker='d')
 
plt.xlabel("Tamanho da entrada")
plt.ylabel("Número de operações")
plt.title("Comparação de complexidade assintótica")
plt.legend()
plt.grid(True)
plt.show()
