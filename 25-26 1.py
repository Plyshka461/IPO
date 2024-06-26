import numpy as np

def det(matrix):
    #Вычисляет определитель матрицы.

    return np.linalg.det(matrix)

def solve(A, b):
    #Решает систему линейных уравнений Ax = b.

    return np.linalg.solve(A, b)
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

det_A = det(A)  # Определитель матрицы A
print("Определитель матрицы A:", det_A)

x = solve(A, b)  # Решение системы уравнений Ax = b
print("Решение системы уравнений:", x)