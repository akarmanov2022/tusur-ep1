from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

X = [4.031, 6.585, 9.452, 0.02247, 0.4946, 4.22, 6.039, 4.144, 6.231, 0.04856]
Y = [148.9, 2129.0, 9910.0, -24.43, -34.09, 208.1, 1439.0, 183.1, 1660.0, -24.82]

z = zip(X, Y)

zs = sorted(z, key=lambda t: t[0])

XP = [z[0] for z in zs]
YP = [z[1] for z in zs]

x = np.linspace(0.04856, 9.452, num=100, endpoint=True)

fig, ax = plt.subplots()

kind_lst = ['linear', 'cubic', 'quadratic']
ax.plot(XP, YP, label="Y", marker="o")
for k in kind_lst:
    f = interpolate.interp1d(XP, YP, kind=k)
    y_new = f(x)
    ax.plot(x, y_new, label=k)

ax.legend(loc="lower right")
plt.show()
