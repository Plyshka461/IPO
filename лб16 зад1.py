class Car:
    def __init__(self, marka, model, vipusk, probeg):#Конструктор инициализирует объект класса с помощью переданных значений
        self._marka = marka
        self._model = model
        self._vipusk = vipusk
        self._probeg = probeg
    @property#Декоратор создает геттер, который позволяет получать значения атрибутов
    def marka(self):
        return self._marka
    @marka.setter#Декоратор создает сеттер, который позволяет изменять значения атрибутов
    def marka(self, new_marka):
        self._marka = new_marka
    @property#Декоратор создает геттер, который позволяет получать значения атрибутов
    def model(self):
        return self._model
    @model.setter#Декоратор создает сеттер, который позволяет изменять значения атрибутов
    def model(self, new_model):
        self._model = new_model
    @property#Декоратор создает геттер, который позволяет получать значения атрибутов
    def vipusk(self):
        return self._vipusk
    @vipusk.setter#Декоратор создает сеттер, который позволяет изменять значения атрибутов
    def vipusk(self, new_vipusk):
        self._vipusk = new_vipusk
    @property#Декоратор создает геттер, который позволяет получать значения атрибутов
    def probeg(self):
        return self._probeg
    @probeg.setter#Декоратор создает сеттер, который позволяет изменять значения атрибутов
    def probeg(self, new_probeg):
        self._probeg = new_probeg
#Создание экземпляра класса
avto = Car("BMW", "X5", 2020, 50000)
#Получение значений свойств через геттеры
print(avto.marka)         # Вывод: BMW
print(avto.model)       # Вывод: X5
print(avto.vipusk)  # Вывод: 2020
print(avto.probeg)       # Вывод: 50000
#Изменение значений свойств через сеттеры
avto.marka = "Audi"
avto.model = "Q7"
avto.vipusk = 2022
avto.probeg = 10000
#Вывод новой информации
print(avto.marka)
print(avto.model)
print(avto.vipusk)
print(avto.probeg)
# Попытка непосредственного изменения свойств
avto.marka = "Mercedes"# Ошибка: AttributeError