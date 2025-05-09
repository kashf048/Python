class Animal(object):
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
print(isinstance(m, Mammal))
print(isinstance(m, object))
o = object()
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
