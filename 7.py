class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 100
    def eat(self):
        self.energy += 10
        print(f"{self.name} je z miski...  Jego energia wynosi {self.energy}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def eat(self):
        super().eat()
        print(f"{self.breed} o imieniu {self.name} merda ogonem z radości!")


if __name__ == '__main__':
    animal = Animal("Zwierzak")
    animal.eat()
    dog = Dog("Burek", "Kundel")
    dog.eat()