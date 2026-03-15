class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} je z miski...")

class Dog(Animal):
    def eat(self):
        super().eat()
        print(f"{self.name} merda ogonem z radości!")


if __name__ == '__main__':
    animal = Animal("Zwierzak")
    animal.eat()
    dog = Dog("Burek")
    dog.eat()