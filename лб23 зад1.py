import numpy as np
# Создаем случайное количество строк и столбцов от 15 до 100
num_rows = np.random.randint(15, 100)
num_columns = np.random.randint(15, 100)
# Заполняем массив случайными целыми числами от 1 до 1000
matrix = np.random.randint(1, 1000, size=(num_rows, num_columns))
# Выводим матрицу на экран
print("Прямоугольный массив:")
print(matrix)
# Находим максимальный элемент в седьмом столбце
max_element = np.max(matrix[:, 6])
print(f"Максимальный элемент в седьмом столбце: {max_element}")
# Вычисляем сумму всех элементов матрицы и найденного элемента
total_sum = np.sum(matrix) + max_element
print(f"Сумма элементов матрицы и найденного элемента: {total_sum}")
