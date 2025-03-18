# Inheritance is a mechanism that allow us to define the common behavior or common functions in one class, (and then inherit them in other classes.)

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish:
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)