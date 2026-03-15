class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = float(grade)
    def __str__(self):
        return f"{self.name} - ocena: {self.grade}"

class Journal:
    def __init__(self):
        self.students = []
    def create(self):
        name = input("Podaj imię: ")
        grade = float(input("Ocena (2-5): "))

        self.students.append(Student(name, grade))
        print("Dodano studenta")
        # dodać zabezpieczenia
        # niepuste imię
        # ocena jest z listy [2,3,3.5,4,4.5,5]
    def read(self):
        # matoda, która wyświetla listę studentów i ich oceny
        pass

    def run(self):
        while True:
            print("=== DZIENNIK ===")
            print("1. Dodaj studenta")
            print("2. Lista studentów")
            print("x. Zakończenie pracy")

            choise = input("Opcja: ")

            if choise == "1":
                self.create()
            elif choise == "2":
                self.read()
            elif choise.lower() == "x":
                print("Do zobaczenia!")
                break
            else:
                print("Niepoprawna opcja!")

if __name__ == '__main__':
    Journal().run()