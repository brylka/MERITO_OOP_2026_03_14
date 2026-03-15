class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} wydaje dźwięk...")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} mówi: HAU HAU!")

if __name__ == '__main__':
    animal = Animal("Zwierzak")
    animal.speak()
    dog = Dog("Burek")
    dog.speak()
