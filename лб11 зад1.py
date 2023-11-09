class SpaceFlight:
#описание информации о космическом полете
    def __init__(self, destination, launch_date, distance, duration, spacecraft, crew):
        self.destination = destination  # Назначение полета
        self.launch_date = launch_date  # Дата запуска
        self.distance = distance  # Пройденное расстояние
        self.duration = duration  # Продолжительность полета
        self.spacecraft = spacecraft  # Информация о космическом корабле
        self.crew = crew  # Список членов экипажа
#обновление продолжительности полета
    def update_duration(self, new_duration):
        self.duration = new_duration
#обновление назначения полета
    def update_destination(self, new_destination):
        self.destination = new_destination
#добавление нового члена экипажа
    def add_crew_member(self, new_member):
        self.crew.append(new_member)
#вывод информации о полете
    def display_info(self):
        print(f"Destination: {self.destination}")
        print(f"Launch Date: {self.launch_date}")
        print(f"Distance: {self.distance} km")
        print(f"Duration: {self.duration} days")
        print(f"Spacecraft: {self.spacecraft}")
        print(f"Crew: {', '.join(self.crew)}")
# Создание экземпляров класса
flight1 = SpaceFlight("Марс", "2023-11-10", 0.5, 1, "Акулёнок", ["Губанова Арина", "Осипова Алиса"])
flight2 = SpaceFlight("Сатурн", "2023-11-11", 1, 9, "Димооооон", ["Терентьев Мирон", "Терентьев Мирон"])
flight3 = SpaceFlight("Уран", "2222-02-22", 600, 1643, "Цыган", ["Новикова Ева", "Лаврова Виктория"])
flight4 = SpaceFlight("Нептун", "2035-12-10", 777, 732, "Медвед", ["Кузнецова Стефания", "Ковалев Артём"])
flight5 = SpaceFlight("Меркурий", "2045-07-19", 666, 69, "Новый миф", ["Гусева Анна", "Волошина Екатерина"])
# Вывод информации о созданных экземплярах
flight1.display_info()
flight2.display_info()
flight3.display_info()
flight4.display_info()
flight5.display_info()