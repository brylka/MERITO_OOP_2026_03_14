class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
    def accelerate(self):
        if self.speed < 120:
            self.speed += 10
        else:
            print(f"Limit prędkości {self.name} osiągnięty!")
    def status(self):
        if self.speed > 0:
            print(f"Samochód {self.name} porusza się z prędkością {self.speed}km/h")
        else:
            print(f"Samochód {self.name} stoi.")
    def honk(self):
        print(f"Samochód {self.name} trąbi")

fiat = Car("Fiat")
bmw = Car("BMW")
audi = Car("Audi")
audi.status()
# bmw.speed = 200
bmw.honk()
for _ in range(20):
    bmw.accelerate()
    bmw.status()



# bmw.status()
#


audi.accelerate()
audi.status()
# bmw.honk()
# fiat.honk()
# audi.status()
# fiat.status()
# # fiat.speed = 500
# fiat.status()
# print(fiat.speed)

