countries = ['Россия', 'Беларусь', 'Китай', 'Нигерия', 'Нигер', 'Германия', 'Зимбабве']#Создаем список из семи стран
countries_tuple = tuple(countries)#Создаем кортеж из списка стран
print("countries_tuple:", countries_tuple)#Выводим результат
new_tu = tuple(countries_tuple[:3])#Создаем новый кортеж new_tu из первых трех элементов кортежа countries_tuple
print("new_tu:", new_tu)#Выводим результат
new_tu2 = tuple(countries_tuple[3:])#Создаем новый кортеж new_tu2 из четырех оставшихся элементов кортежа countries_tuple
print("new_tu2:", new_tu2)#Выводим результат
all_tu = (countries_tuple, new_tu, new_tu2)#Создаем кортеж all_tu, который содержит все созданные кортежи
print("all_tu:", all_tu)#Выводим значения всех кортежей