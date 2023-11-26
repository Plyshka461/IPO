class Drob:
    """ Класс, представляющий дроби """
    def __init__(self, a=0, b=1):
        """ Инициализация объекта """
        self.a = a
        self.b = b
        self.normalize()
    def normalize(self):
        """ Нормализация дроби """
        gcd = self.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd
    def gcd(self, a, b):
        """ Нахождение наибольшего общего делителя """
        while b:
            a, b = b, a % b
        return a
    def __str__(self):
        """ Представление дроби в виде строки """
        return f"{self.a}/{self.b}"
    def __eq__(self, other):
        """ Проверка на равенство """
        return self.a == other.a and self.b == other.b
    def __lt__(self, other):
        """ Проверка на меньше """
        return self.a * other.b < other.a * self.b
    def __add__(self, other):
        """ Сложение двух дробей """
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Drob(a, b)
    def __sub__(self, other):
        """ Вычитание двух дробей """
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Drob(a, b)
    def __mul__(self, other):
        """ Умножение двух дробей """
        a = self.a * other.a
        b = self.b * other.b
        return Drob(a, b)
    def __truediv__(self, other):
        """ Деление двух дробей """
        a = self.a * other.b
        b = self.b * other.a
        return Drob(a, b)
# Создание двух дробей
d1 = Drob(2, 3)
d2 = Drob(3, 4)
# Проверка на равенство
print(d1 == d2)
# Проверка на меньше
print(d1 < d2)
# Сложение
print(d1 + d2)
# Вычитание
print(d1 - d2)
# Умножение
print(d1 * d2)
# Деление
print(d1 / d2)