class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduse(self):
        return print (f"привет меня зовут {self.name}")


kirito = Hero("Kirito", 100, 1000)

kirito.introduse()

print(kirito.hp)
