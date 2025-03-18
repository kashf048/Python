class Animal(object):
    def __init__(self):
        print("Animal Consturctor")
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        print("Mammal Consturctor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish:
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)