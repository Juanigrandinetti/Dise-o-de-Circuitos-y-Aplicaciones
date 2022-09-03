from turtle import color
import numpy as np
import matplotlib.pyplot as plt

f = [10]
j = 10
for i in range(5):
    f.append(j*10)
    j = 10*j

Av = [10, 10, 10, 10, 10, 5]
plt.plot(f, Av, label = '|Av(f)|', color = 'black')
plt.yticks(np.arange(0, 11, step = 2.5))
plt.vlines(x = 1e5, ymin = 0, ymax = 10, label = 'fc = 100KHz', color = 'black', linestyles = '--')
plt.legend()
plt.fill_between([0, 1e5], 0, 10, color = 'lightgreen')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Av')
plt.grid()
plt.show()