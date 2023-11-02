# Вводим N
N = int(input("Введите количество чисел: "))
# Открываем файл для записи
file = open(f"file1_{N}.txt", "w")
# Вводим числа и записываем их в файл
for i in range(N):
    num = int(input(f"Введите число {i+1}: "))
    file.write(str(num) + "\n")
# Закрываем файл
file.close()
# Открываем файл для чтения
file_read = open(f"file1_{N}.txt", "r")
# Открываем файл для записи
file_write = open(f"file2_{N}.txt", "w")
# Читаем числа из первого файла и записываем на четных позициях во второй файл
numbers = file_read.readlines()
for i in range(len(numbers)):
    if i % 2 == 1:
        file_write.write(numbers[i])
# Закрываем файлы
file_read.close()
file_write.close()