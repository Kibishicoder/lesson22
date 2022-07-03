# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def room_num(self):
        return 42


class Street:
    def get_room(self) -> Room:
        print(Room)
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def get_population(self):
        print(City.get_population())
        return 100500


class Country:
    def get_population(self) -> City:
        print(City)
        return City()


class Planet:
    def get_population(self) -> Country:
        print(Country)
        return Country()


class Person:
    def __init__(self, city_population, room_num):
        self.city_population = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.


print(Person.get_person_room())





