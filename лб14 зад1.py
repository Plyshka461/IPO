class Apteka:
    def __init__(self, nazva, adres, gorod, direktor):#Конструктор класса принимает четыре аргумента и инициализирует соответствующие атрибуты объекта
        self.nazva = nazva
        self.adres = adres
        self.gorod = gorod
        self.direktor = direktor

class Klients(Apteka):#Конструктор класса принимает пять аргумента и инициализирует соответствующие 4 атрибута объекта
    def __init__(self, nazva, familia, imya, otchestvo, skidka):
        super().__init__(nazva, 'Секрет', 'Еще больший секрет', 'Ну я не знаю')
        self.familia = familia
        self.imya = imya
        self.otchestvo = otchestvo
        self.skidka = skidka

class FondApteki(Apteka):
    def __init__(self, nazva, nazva_lekarstva, tip_lekarstva, tsena, strana):#Конструктор класса принимает пять аргумента и инициализирует соответствующие 4 атрибута объекта
        super().__init__(nazva, 'Не скажу', 'Не выдаем', 'А то будете конкурентами')
        self.nazva_lekarstva = nazva_lekarstva
        self.tip_lekarstva = tip_lekarstva
        self.tsena = tsena
        self.strana = strana

class Prodazhi(Apteka):#Конструктор класса принимает шесть аргумента и инициализирует соответствующие 5 атрибутов объекта
    def __init__(self, nazva, nazva_lekarstva, tsena, klient, shuk, summa):
        super().__init__(nazva, 'ул. Сталина, 10', 'Подошмяненск', 'Я Не Знаю')
        self.nazva_lekarstva = nazva_lekarstva
        self.tsena = tsena
        self.klient = klient
        self.shuk = shuk
        self.summa = summa
# Создание экземпляров классов
apteka_1 = Apteka("Аптека №1", "ул. Сталина, 10", "Подошмяненск", "Я Не Знаю")
klient_1 = Klients("Аптека №1", "Петров", "Пётр", "Петрович", -15)
lekarstvo_1 = FondApteki("Аптека №1", "Аспирин", "Обезболивающее", 100, "Россия")
prodazha_1 = Prodazhi("Аптека №1", "Аспирин", 100, "Петров Пётр Петрович", 2, 200)
# Вывод информации о каждом экземпляре с помощью соответствующих методов
print(apteka_1.__dict__)
print(klient_1.__dict__)
print(lekarstvo_1.__dict__)
print(prodazha_1.__dict__)