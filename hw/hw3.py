# class Student:
#
#     def __init__(self, name, grade, password):
#         self.name = name
#         self._grade = grade
#         self.__password = password
#
#     def change_password(self, new_pass):
#         self.__password = new_pass
#         return print ("новый пароль")
#
#     def get_info(self):
#         print(f" {self.name}, {self._grade}")
#
#
# student = Student("myky", "99", "qwerty")
# student.get_info()
# student.change_password("12344321")



from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def move(self):
        print("машина едет")

    def stop(self):
        print("машина остановилась")


class Bike(Vehicle):
    def move(self):
        print("мотоцикл едет")

    def stop(self):
        print("мотоцикл остановился")

car = Car()
bike = Bike()

car.move()
bike.move()

car.stop()
bike.stop()

