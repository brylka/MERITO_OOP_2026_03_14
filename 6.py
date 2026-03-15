class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} wydaje dźwięk...")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} mówi: HAU HAU!")
    def fetch(self):
        print(f"{self.name} aportuje piłkę!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} mówi: MIAU MIAU!")
    def purr(self):
        print(f"{self.name} mruczy...")

if __name__ == '__main__':
    animal = Animal("Zwierzak")
    animal.speak()
    dog = Dog("Burek")
    dog.speak()
    dog.fetch()
    cat = Cat("Mruczek")
    cat.speak()
    cat.purr()

# dodać kolejną klasę, która dziedziczy czy Animal lub innej klasie
# potestować czy dziedziczą się metody z danej klasy