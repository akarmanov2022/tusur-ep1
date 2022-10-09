import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

x, y = np.meshgrid(np.linspace(-100, 100, 10), np.linspace(-100, 100, 10))
z = (x - x * y) / (x ** 2 + y * np.sin(x * y))

figure = plt.figure()
ax = figure.add_subplot(projection='3d')
ax.plot_surface(x, y, z)

plt.title('Поверхности. Вариант 12.')
plt.xlabel('X')
plt.ylabel('Y')
plt.clabel('Z')
plt.show()
