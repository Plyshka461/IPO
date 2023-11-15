class SpaceFlight:
    #описание информации о космическом полете
    def __init__(self, destination=None, launch_date=None, distance=None, duration=None, spacecraft=None, crew=None):
        self.destination = destination  # Назначение полета
        self.launch_date = launch_date  # Дата запуска
        self.distance = distance  # Пройденное расстояние
        self.duration = duration  # Продолжительность полета
        self.spacecraft = spacecraft  # Информация о космическом корабле
        self.crew = crew if crew is not None else []  # Список членов экипажа
    #сеттер для обновления продолжительности полета
    def set_duration(self, new_duration):
        self.duration = new_duration
    #сеттер для обновления назначения полета
    def set_destination(self, new_destination):
        self.destination = new_destination
    #метод для добавления нового члена экипажа
    def add_crew_member(self, new_member):
        self.crew.append(new_member)
    #вывод информации о полете
    def display_info(self):
        print(f"Планета: {self.destination}")
        print(f"Дата отправления: {self.launch_date}")
        print(f"Расстояние: {self.distance} km")
        print(f"Продолжительность: {self.duration} days")
        print(f"Корабль: {self.spacecraft}")
        print(f"Участники: {', '.join(self.crew)}")
    #деструктор
    def __del__(self):
        print("Деструктор вызвал космический полет")
# Создание экземпляров класса с использованием конструктора
flights = []
for _ in range(10):
    destination = input("Введите планету: ")
    launch_date = input("Введите дату отправления: ")
    distance = float(input("Введите дистанцию: "))
    duration = int(input("Введите продолжительность полета: "))
    spacecraft = input("Введите название корабля: ")
    crew = input("Введите имена летчиков(через запятую): ").split(", ")
    flight = SpaceFlight(destination, launch_date, distance, duration, spacecraft, crew)
    flights.append(flight)
# Вывод информации о созданных экземплярах
for flight in flights:
    flight.display_info()