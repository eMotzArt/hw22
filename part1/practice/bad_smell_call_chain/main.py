# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

# class Room:
#     def get_name(self):
#         return 42
#
#
# class Street:
#     def get_room(self) -> Room:
#         return Room()
#
#
# class City:
#     def get_street(self) -> Street:
#         return Street()
#
#     def population(self):
#         return 100500
#
#
# class Country:
#     def get_city(self) -> City:
#         return City()
#
#
# class Planet:
#     def get_contry(self) -> Country:
#         return Country()
#
#
# class Person:
#     def __init__(self):
#         self.planet = Planet()
#
#     def get_person_room(self):
#         return self.planet.get_contry().get_city().get_street().get_room().get_name()
#
#     def get_city_population(self):
#         return self.planet.get_contry().get_city().population()


#MY_SOLUTION
class Person:
    def __init__(self, room: int, city_population: int):
        self._room = room
        self._city_population = city_population

    def get_person_room(self) -> int:
        return self._room

    def get_city_population(self) -> int:
        return self._city_population

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(11, 234567)
print(person.get_person_room())
print(person.get_city_population())

