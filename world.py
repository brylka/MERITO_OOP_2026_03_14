from car import Car


class World:
    def __init__(self):
        self.cars = []
        print("Świat został stworzony!")
    def cars_list(self):
        for i, car in enumerate(self.cars):
            print(f"{i}. {car.name} prędkość: {car.speed}km/h")
    def get_car_by_number(self, number):
        try:
            car = self.cars[number]
        except IndexError:
            car = None
        return car
    def run(self):
        while True:
            print("1. Dodaj samochód")
            print("2. Lista samochodów")
            print("3. Przyspiesz samochód")
            print("4. Zahamuj samochód")
            print("5. Zderz samochody")
            try:
                choice = int(input("Wybierz opcję: "))
            except ValueError:
                print("Podaj liczbę!")
                choice = 0
            if choice == 1:
                car_name = input("Podaj markę samochodu: ")
                car = Car(car_name)
                self.cars.append(car)
            elif choice == 2:
                if not self.cars:
                    print("Brak samochodów w świecie!")
                else:
                    self.cars_list()
            elif choice == 3:
                self.cars_list()
                car_number = int(input(f"Który samochód przyspieszyć (0-{len(self.cars)-1}): "))
                try:
                    self.get_car_by_number(car_number).accelerate()
                except AttributeError:
                    print("Nie ma takiego samochodu")
            elif choice == 4:
                self.cars_list()
                car_number = int(input(f"Który samochód przyhamować (0-{len(self.cars)-1}): "))
                self.get_car_by_number(car_number).brake()
            elif choice == 5:
                self.cars_list()
                car_number_1 = int(input(f"Króry samochód: "))
                car_number_2 = int(input(f"Z którym samochodem: "))
                self.get_car_by_number(car_number_1).crash(self.get_car_by_number(car_number_2))


if __name__ == '__main__':
    World().run()