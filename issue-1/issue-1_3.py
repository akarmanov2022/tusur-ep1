import math
from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0, 2 * math.pi, 100)
print(t)

a = 8
b = 4

x = (a + b) * np.cos(t) - a * np.cos((a + b) - t / a)
y = (a + b) * np.sin(t) - a * np.sin((a + b) - t / a)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.title("Параметрически заданные функции. Вариант 2.")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
