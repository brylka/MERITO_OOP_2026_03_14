class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age
    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age

dog = Dog("Burek", 5)
print(dog.name)
print(dog.age)
dog.set_age(8)
print(dog.get_age())
dog.age = -10
print(dog.get_age())