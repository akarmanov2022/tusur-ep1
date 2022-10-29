import numpy as np
import copy


def ConsoleOutput(matrix, solutions):
    print("--- Решение СЛАУ методом Гаусса ---")
    print("Initial matrix = \n", A)
    print("B = \n", np.reshape(B, (N, 1)))
    print("Triangular view = \n", matrix)
    print("Solutions: ")
    for i in range(N - 1, -1, -1):
        print("x" + str(i + 1) + " =", solutions[i])


def MaxDiagonalElementInColumn(current, matrix):
    m = matrix[current][current]
    n_row = current

    for i in range(current, N):
        if m < matrix[i][current]:
            m = matrix[i][current]
            n_row = i

    return n_row


def SystemSolutionReverse(matrix, b):
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

    ConsoleOutput(matrix, solutions)


def SystemSolutionStraight():
    matrix = copy.copy(A)
    b = copy.copy(B)

    for i in range(N):
        # Чтобы избежать случаев, когда в диагонале появляются нули,
        # я переношу максимальную строку со значением по колонке, вверх
        nrow_max = MaxDiagonalElementInColumn(i, matrix)

        # Проверяю, что найденная строка в функции не есть текущая
        if nrow_max != i:
            temp = copy.copy(matrix[i])
            matrix[i] = copy.copy(matrix[nrow_max])
            matrix[nrow_max] = temp

            temp_b = copy.copy(b[i])
            b[i] = copy.copy(b[nrow_max])
            b[nrow_max] = temp_b

        # Чтобы добиться единицы в диагонали я беру диагональный элемент
        diag_elem = matrix[i][i]

        # И делю всю строку на него
        for j in range(N):
            matrix[i][j] = matrix[i][j] / diag_elem

        b[i] = b[i] / diag_elem

        # А после элементарными преобразованиями преобразую матрицу в треугольный вид
        for j in range(i + 1, N):
            diagonal = matrix[j][i]

            for k in range(N):
                matrix[j][k] = matrix[j][k] - diagonal * matrix[i][k]

            b[j] = b[j] - diagonal * b[i]

    # Обратный ход
    SystemSolutionReverse(matrix, b)


N = 6
A = np.array([[-10., -13., 13., -1., 1., 1.],
              [-5., -4., -14., 16., -1., -2.],
              [-1., -2., 15., 4., 0., -5.],
              [-14., 7., -6., -4., -6., -13.],
              [14., -9., -3., -3., -5., -10.],
              [-14., 1., 3., 6., -8., -6.]])
B = np.array([106., 84., 9., 91., -47., 111.])

SystemSolutionStraight()
