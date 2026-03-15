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
        if not self.students:
            print("Lista jest pusta")
            return
        print("Lista studentów:")
        for i, s in enumerate(self.students):
            print(f"{i+1}. {s}")
    def update(self):
        pass
        # dodać możliwość edycji oceny studenta
    def delete(self):
        pass
        # dodać możliwość usuwania studenta

    def run(self):
        while True:
            print("=== DZIENNIK ===")
            print("1. Dodaj studenta")
            print("2. Lista studentów")
            print("3. Edycja studenta")
            print("4. Usuwanie studenta")
            print("x. Zakończenie pracy")

            choise = input("Opcja: ")

            if choise == "1":
                self.create()
            elif choise == "2":
                self.read()
            elif choise == "3":
                self.update()
            elif choise == "4":
                self.delete()
            elif choise.lower() == "x":
                print("Do zobaczenia!")
                break
            else:
                print("Niepoprawna opcja!")

if __name__ == '__main__':
    Journal().run()