import numpy as np
# Создание двумерного массива из случайных чисел с нормальным распределением
arr_2d = np.random.normal(loc=0, scale=1.0, size=(3, 4))
print("Двумерный массив:")
print(arr_2d)
print()
# Получение одномерного массива из двумерного
arr_1d = arr_2d.flatten()
print("Одномерный массив:")
print(arr_1d)
print()
# Проверка атрибута size
print("Размер двумерного массива:", arr_2d.size)
print("Размер одномерного массива:", arr_1d.size)
