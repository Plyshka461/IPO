n=int(input("Введите число: "))#Вводим число
prost=list(range(n+1)) #Преобразование последовательности в список
prost[1]=0 #Обнуление 1 (это не простое число)
for i in range(n+1): #Перебор всех элементов
    if prost[i]!=0: #Выбор только ненулевых(невычеркнутых) элементов
        for j in range(i+i,n+1,i): #Вычеркивание элементов по правилу Эратосфена
            prost[j]=0# Устанавливаем значение непростых чисел в 0
for i in range(n+1): #Вывод элементов не равных 0
    if prost[i]!=0: # Если текущее число не равно нулю
        print(prost[i])# Выводим простое число
n=int(input("Введите число: "))# Ввод числа от пользователя
prost=list(range(n+1))# Создание списка чисел от 0 до n
prost[1]=0# Простое число 1 не является простым, поэтому его значение устанавливается в 0
for i in range(n+1):# Цикл по всем числам от 0 до n
    if prost[i]!=0:# Если текущее число не равно нулю (т.е. простое число)
        for j in range(i+i,n+1,i):# Цикл от текущего числа с шагом i до n с шагом i
            prost[j]=0# Устанавливаем значение непростых чисел в 0
# Преобразование списка в множество
prost_set = set(prost)
# Удаление 0 из множества
prost_set.remove(0)
# Вывод множества
for num in prost_set:
    print(num)