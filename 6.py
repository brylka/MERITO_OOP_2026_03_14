class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} wydaje dźwięk...")

class Dog(Animal):
    pass

if __name__ == '__main__':
    animal = Animal("Zwierzak")
    animal.speak()
    dog = Dog("Burek")
    dog.speak()
