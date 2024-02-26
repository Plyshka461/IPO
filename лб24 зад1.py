import numpy as np

# Пример одномерного массива числовых значений, включая нулевые элементы
array = np.random.randint(0, 10, size=10)

# Исключение нулевых элементов из массива
non_zero_array = array[array != 0]

# Вывод исходного и преобразованного массива без нулей
print("Исходный массив:")
print(array)

print("\nМассив без нулей:")
print(non_zero_array)
