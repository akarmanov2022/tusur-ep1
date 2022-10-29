import numpy as np
import math

# Вариант 12.
X1 = 47.32
X2 = -26.85
N = 5
M = 3

N_A = 5
M_A = 5

N_B = 5
M_B = 5

N_C = 5
M_C = 5

N_D = 5
M_D = 5

N_E = 5
M_E = 5

A = np.random.random((N_A, M_A))
B = np.random.random((N_B, M_B))
C = np.random.random((N_C, M_C))
D = np.random.random((N_D, M_D))
E = np.random.random((N_E, M_E))

print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
print("E = ", E)

# 1.3
g = np.matmul(np.matmul(C, E) - np.matmul(A, D), B) - np.matmul(A, C)
print("G = \n", g)
# 1.4.1, 1.4.2
g = g + X1 - X2
print("G + X1 - X2 = \n", g)
# 1.4.3
detG = np.linalg.det(g)
print("det G = \n", detG)
# 1.4.4
invG = np.linalg.inv(g)
print("Inv G = \n", invG)
print("Checking the matrix = \n", np.round(np.matmul(invG, g), 0))
# 1.4.5
# w - собственные чи сла, v - собственные векторы
w, v = np.linalg.eig(g)
print("W = \n", w)
print("V = \n", v)
# произведения матрицы на собственный вектор должно быть
# равно произведению собственного числа на собственный вектор.
print("Checking G * v = \n", np.matmul(g, v))
print("Checking w * v = \n", w * v)
# 1.4.6
r = np.linalg.matrix_rank(g)
print("rank =", r)

# 1.4.7
a = g[N - 1]
b = g[:, M - 1]
print("A→ = ", a)
print("B→ = ", b)

# 1.4.7.1
normA = np.linalg.norm(a)
normB = np.linalg.norm(b)

print("|A| = ", normA)
print("|B| = ", normB)

# 1.4.7.2
ortA = a / normA
ortB = b / normB
print("Ort A =", ortA)
print("Ort B =", ortB)

# Ортом A называется вектор, модуль которого равен единице
print("Checking ort A = ", np.round(np.linalg.norm(ortA)))
print("Checking ort B = ", np.round(np.linalg.norm(ortB)))

# 1.4.7.3
print("Sum vectors = ", np.sum(a) + np.sum(b))

# 1.4.7.4
print("Count positive values in A = ", len(a[a >= 0]))
print("Count negative values in A = ", len(a[a < 0]))
print("Count positive values in B = ", len(b[b >= 0]))
print("Count negative values in B = ", len(b[b < 0]))

# 1.4.7.5
print("Scalar product of vectors = ", np.dot(a, b))

# 1.4.7.6
y = math.acos(np.dot(a, b) / (normA * normB))

print("cos(y) =", math.cos(y))
print("sin(y) = ", math.sin(y))

# 1.4.7.7
print("cross product of vectors = ", normA * normB * math.sin(y))

# 1.4.7.8
print("multiplication of vector coordinates = \n", np.multiply(a, b))
