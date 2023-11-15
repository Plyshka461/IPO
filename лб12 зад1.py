class Student:#Создание класса
#инициализатор класса
    def __init__(self, name, group_number, performance):
        self.name = name
        self.group_number = group_number
        self.performance = performance
#Основная функция программы
def main():
    students = []#Создание пустого списка
#ввод данных о студентах
    for _ in range(10):
        name = input("Введите фамилию и инициалы студента: ")
        group_number = input("Введите номер группы: ")
        performance = []#Создание пустого массива для хранения успеваемости
#Цикл для ввода оценок успеваемости
        for i in range(5):
            mark = int(input(f"Введите успеваемость студента (оценка {i+1}): "))
            performance.append(mark)
        student = Student(name, group_number, performance)#объект с введенными данными
        students.append(student)
#Формирование списка содержащего студентов с хотя бы одной неудовлетворительной отметкой
    ploxie_students = [student for student in students if any(mark < 3 for mark in student.performance)]
#Вывод всех студентов
    if ploxie_students:
        print("Студенты с неудовлетворительной успеваемостью:")
        for student in ploxie_students:
            print(f"{student.name}, группа {student.group_number}")
    else:
        print("Нет студентов с неудовлетворительной успеваемостью.")
if __name__ == "__main__":
    main()