class Rub(object):
    """ Класс для работы с рублями и копейками."""
    def __init__(self, rub=0, kop=0):#Конструктор класса принимает два аргумента и инициализирует соответствующие атрибуты объекта.
        self.rub = rub
        self.kop = kop
    def __str__(self):#Метод переопределен для класса и возвращает строковое представление объекта в формате "rub.kop rub"
        if self.kop < 10:
            kop_str = '0' + str(self.kop)
        else:
            kop_str = str(self.kop)
        return f"{self.rub}.{kop_str} rub"
    def __lt__(self, other):#Метод переопределен для класса и позволяет сравнивать объекты типа Rub, возвращает True, если текущий объект меньше объекта other и False в противном случае
        if self.rub < other.rub:
            return True
        elif self.rub == other.rub and self.kop < other.kop:
            return True
        else:
            return False
    def __add__(self, other):#Метод переопределен для класса и позволяет сложить два объекта типа Rub. Он возвращает новый объект типа Rub, в котором суммарное количество рублей и копеек равно сумме соответствующих значений текущего объекта и объекта other
        total_rub = self.rub + other.rub
        total_kop = self.kop + other.kop
        if total_kop >= 100:
            total_rub += 1
            total_kop -= 100
        return Rub(total_rub, total_kop)
class Goods(object):
    """ Класс описания товара: название и цена"""
#Класс имеет два атрибута name и price
    def __init__(self, name='', rub=0, kop=0):
        self.name = name
        self.price = Rub(rub, kop)
#создаются две переменные
student_orders = []
total_cost = Rub()
#используется цикл для ввода списка покупок от студента, затем создается объект класса, используя полученные значения, и добавляется в список
while True:
    order = input("Введите название товара и его стоимость в формате 'название rrr.kk rub' (для выхода введите 'выход'): ")
    if order == 'выход':
        break
    else:
        name, price_str = order.split()
        rub_str, kop_str = price_str.split('.')
        rub = int(rub_str)
        kop = int(kop_str)
        student_orders.append(Goods(name, rub, kop))#список заказов студента
        total_cost += Rub(rub, kop)#общая стоимость заказов
# Сортировка товаров
student_orders.sort(key=lambda x: x.price, reverse=True)
# Вывод списка товаров и их стоимости
for goods in student_orders:
    print(f"{goods.name}: {goods.price}")
# Вывод общей стоимости обеда
print(f"Общая стоимость обеда: {total_cost}")