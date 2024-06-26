import numpy as np
# Создание одномерного массива A
A = np.arange(12, 24)
print("Одномерный массив A:")
print(A)
print()
# Создание двумерных массивов из массива A
print("Двумерные массивы из массива A:")
# Двумерный массив 3x4
A_3x4 = A.reshape(3, 4)
print("Форма 3x4:")
print(A_3x4)
print()
# Двумерный массив 4x3
A_4x3 = A.reshape(4, 3)
print("Форма 4x3:")
print(A_4x3)
print()
# Двумерный массив 2x6
A_2x6 = A.reshape(2, 6)
print("Форма 2x6:")
print(A_2x6)
print()
# Двумерный массив 6x2
A_6x2 = A.reshape(6, 2)
print("Форма 6x2:")
print(A_6x2)
print()
