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


class World:
    def __init__(self):
        self.cars = []
        print("Świat został stworzony!")
    def run(self):
        while True:
            print("1. Dodaj samochód")
            print("2. Lista samochodów")
            choice = int(input("Wybierz opcję: "))
            if choice == 1:
                car_name = input("Podaj markę samochodu: ")
                car = Car(car_name)
                self.cars.append(car)
            elif choice == 2:
                print(self.cars)



World().run()