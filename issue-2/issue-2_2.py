import numpy as np
import copy


def max_diagonal_element_column(current, matrix):
    m = matrix[current][current]
    n_row = current

    for i in range(current, N):
        if m < matrix[i][current]:
            m = matrix[i][current]
            n_row = i

    return n_row


def reverse(matrix, b):
    solutions = [0, 0, 0, 0, 0, 0]

    for i in range(N - 1, -1, -1):
        if (N - 1) == i:
            solutions[i] = round(b[i])
            continue

        s = 0
        for j in range(N):
            s = s + matrix[i][j] * solutions[j]

        s = b[i] - s

        solutions[i] = round(s)

    return solutions


def solve_by_the_gaus_method(A, B):
    matrix = copy.copy(A)
    b = copy.copy(B)

    for i in range(N):
        nrow_max = max_diagonal_element_column(i, matrix)

        if nrow_max != i:
            temp = copy.copy(matrix[i])
            matrix[i] = copy.copy(matrix[nrow_max])
            matrix[nrow_max] = temp

            temp_b = copy.copy(b[i])
            b[i] = copy.copy(b[nrow_max])
            b[nrow_max] = temp_b

        diag_elem = matrix[i][i]

        for j in range(N):
            matrix[i][j] = matrix[i][j] / diag_elem

        b[i] = b[i] / diag_elem

        for j in range(i + 1, N):
            diagonal = matrix[j][i]

            for k in range(N):
                matrix[j][k] = matrix[j][k] - diagonal * matrix[i][k]

            b[j] = b[j] - diagonal * b[i]
    print("Треугольный вид: ", matrix)
    return reverse(matrix, b)


N = 6
A = np.array([[-10., -13., 13., -1., 1., 1.],
              [-5., -4., -14., 16., -1., -2.],
              [-1., -2., 15., 4., 0., -5.],
              [-14., 7., -6., -4., -6., -13.],
              [14., -9., -3., -3., -5., -10.],
              [-14., 1., 3., 6., -8., -6.]])
B = np.array([106., 84., 9., 91., -47., 111.])

print("--- Решение СЛАУ методом Гаусса ---")
print("A = ", A)
print("B = ", np.reshape(B, (N, 1)))
solutions = solve_by_the_gaus_method(A, B)
print("Решение: ", solutions)
