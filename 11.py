class Student:
    def __init__(self, name, grade):
        GRADE_LIST = [2,3,3.5,4,4.5,5]
        if not name:
            raise ValueError("Imię nie może być puste!")
        if grade not in GRADE_LIST:
            raise ValueError(f"Ocena musi być jedną z: {GRADE_LIST}")
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
        try:
            self.students.append(Student(name, grade))
            print("Dodano studenta")
        except ValueError as e:
            print(e)
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