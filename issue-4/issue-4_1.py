# Интегрирование. Определенный интеграл. Вариант 19.
from scipy import integrate
from matplotlib import pyplot as plt
import numpy as np


def f(x):
    return 1 / (1 + 2 * np.sin(x) ** 2)


v, err = integrate.quad(f, 0, np.pi / 4)
x = []
y = []
h = 0
print("solution =", v)
while h < np.pi / 4:
    x.append(h)
    y.append(f(h))
    h += 0.001
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()

ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()
