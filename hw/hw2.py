class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"ransport is moving")


class Car(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel

    def move(self):
        super().move()
        print("Car is driving")

class Plane(Transport):
    def __init__(self, name, speed, wings):
        super().__init__(name, speed)
        self.wings = wings

    def move(self):
        super().move()
        print("Plane is flying")

class Boat(Transport):
    def __init__(self, name, speed, sail):
        super().__init__(name, speed)
        self.sail = sail

    def move(self):
        super().move()
        print("Boat is driving")


car = Car(name="BMW", speed=160, fuel=92)
plane = Plane(name="Boing", speed=2000, wings=2)
boat = Boat(name="cr7", speed=250, sail="water" )

car.move()
plane.move()
boat.move()

