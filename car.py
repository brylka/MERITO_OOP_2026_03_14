class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.alive = True
    def accelerate(self):
        if not self.alive:
            print(f"Samochód {self.name} jest popsuty!")
        elif self.alive and self.speed < 120:
            self.speed += 10
            print(f"Samochód {self.name} przyspiesza i jedzie z prędkością {self.speed}km/h")
        else:
            print(f"Limit prędkości {self.name} osiągnięty!")
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
    def crash(self, other_car):
        if self.speed > 0:
            print(f"Samochód {self.name} zderza się z samochodem {other_car.name}")
            self.alive = False
            other_car.alive = False
            self.speed = 0
            other_car.speed = 0
        else:
            print(f"Samochód {self.name} się nie porusza i nie może się zderzać!")
    def status(self):
        if self.speed != 0:
            print(f"Samochód {self.name} porusza się z prędkością {self.speed}km/h")
        else:
            print(f"Samochód {self.name} stoi.")
    def honk(self):
        print(f"Samochód {self.name} trąbi")

if __name__ == '__main__':
    bmw = Car("BMW")
    bmw.accelerate()
    bmw.status()