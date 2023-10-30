import math#импортируем модуль math
def calculate_median(a, b, c):#объявляем функцию с тремя параметрами a, b, c
    median_a = math.sqrt((2 * b ** 2 + 2 * c ** 2 - a ** 2) / 4)#вычисляем медиану, проведенную к стороне a
    median_b = math.sqrt((2 * a ** 2 + 2 * c ** 2 - b ** 2) / 4)#вычисляем медиану, проведенную к стороне b
    median_c = math.sqrt((2 * a ** 2 + 2 * b ** 2 - c ** 2) / 4)#вычисляем медиану, проведенную к стороне c
    return median_a, median_b, median_c#возвращаем значения медиан median_a, median_b, median_c в виде кортежа
#ввод значений
a = 6
b = 9
c = 3
medians = calculate_median(a, b, c)#присваиваем вычесленные значения значению medians
print(medians)#вывод результата