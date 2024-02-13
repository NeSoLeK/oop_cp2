
class Gun:
    def __init__(self):
        self.reload()

    def fire(self):
        self.ammo_count -= 1

    def reload(self):
        self.ammo_count = 10


class Person:
    def __init__(self, gun_left, gun_right):
        self.gun_left = gun_left
        self.gun_right = gun_right

    def fire(self):
        self.gun_left.fire()
        self.gun_right.fire()


gun1 = Gun()
gun2 = Gun()
kirill = Person(gun1, gun2)
