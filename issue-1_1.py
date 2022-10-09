import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def fn(x):
    if x >= 0:
        return x / (math.pow(x, 2) + 10)
    else:
        return math.sin(x + 2) / math.pow(x, 2) + 4


fig, ax = plt.subplots()

x = np.linspace(-100, 100, 100)
y = []

for i in x:
    y.append(fn(i))

ax.plot(x, y)

plt.title("")
plt.show()
