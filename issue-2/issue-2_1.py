import numpy as np

A = [[-4, -1, -1, 6],
     [4, 8, 8, 0],
     [-2, -1, 8, -2],
     [6, 1, 8, 0]]
B = [-36, -8, -19, -11]

detA = np.linalg.det(A)
print(detA)


def get_sub_det(matrix_a, matrix_b, index: int):
    temp = list()
    for i in range(len(matrix_a)):
        copy_row = list(matrix_a[i])
        copy_row[index] = matrix_b[i]
        temp.append(copy_row)
    print(temp)
    return np.linalg.det(temp)


detA1 = get_sub_det(A, B, 0)
print(detA1)
detA2 = get_sub_det(A, B, 1)
print(detA2)
detA3 = get_sub_det(A, B, 2)
print(detA3)
detA4 = get_sub_det(A, B, 3)
print(detA4)
print(A)
X = [
    (detA1 / detA).__round__(),
    (detA2 / detA).__round__(),
    (detA3 / detA).__round__(),
    (detA4 / detA).__round__()
]
print(X)
