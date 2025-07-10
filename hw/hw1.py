class Auto:
    def __init__(self, name, speed, power):
        self.name = name
        self.speed = speed
        self.power = power

    def action(self):
        return print(f"авто марка: {self.name}")

bmw = Auto("BMW", 180, 300)
mersedes = Auto(name="Mersedes", speed=160, power=250)

bmw.action()
mersedes.action()

print(bmw.name, bmw.speed, )
print(mersedes.name, mersedes.speed, )