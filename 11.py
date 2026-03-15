import json


class Student:
    def __init__(self, name, grade):
        GRADE_LIST = [2,3,3.5,4,4.5,5]
        if not name:
            raise ValueError("Imię nie może być puste!")
        if grade not in GRADE_LIST:
            raise ValueError(f"Ocena musi być jedną z: {GRADE_LIST}")
        self.name = name
        self.grade = float(grade)
    def update_grade(self, new_grade):
        pass
    def to_dict(self):
        return {"name": self.name, "grade": self.grade}
    def __str__(self):
        return f"{self.name} - ocena: {self.grade}"

class Journal:
    def __init__(self):
        self.students = []
        self.FILE = "students.json"
        self.load()

    def save(self):
        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f)

    def load(self):
        try:
            with open(self.FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = [Student(s["name"], s["grade"]) for s in data]
            print("Dane zostały wczytane!")
        except FileNotFoundError:
            print("Brak pliku")

    def create(self):
        name = input("Podaj imię: ")
        grade = float(input("Ocena (2-5): "))
        try:
            self.students.append(Student(name, grade))
            self.save()
            print("Dodano studenta")
        except ValueError as e:
            print(e)

    def read(self):
        if not self.students:
            print("Lista jest pusta")
            return
        print("Lista studentów:")
        for i, s in enumerate(self.students):
            print(f"{i+1}. {s}")

    def update(self):
        self.read()
        if not self.students:
            return
        try:
            number = int(input("Podaj numer studenta do edycji: "))
            if not 1 <= number <= len(self.students):
                print("Zły numer!")
                return
            student = self.students[number - 1]
            new_grade = float(input(f"Podaj nową ocenę dla {student.name} (aktualna {student.grade}): "))
            student.grade = new_grade
            self.save()
            print(f"Zaktualizowano ocenę studentowi {student.name} na ocenę {student.grade}")
        except ValueError:
            print("Niepoprawne dane!")
        # ewentualnie dodać możliwość zmiany imienia studenta

    def delete(self):
        self.read()
        if not self.students:
            return
        try:
            number = int(input("Podaj numer studenta do usunięcia: "))
            if not 1 <= number <= len(self.students):
                print("Zły numer!")
                return
            self.students.pop(number - 1)
            self.save()
            print("Usunięto studenta!")
        except ValueError:
            print("Niepoprawne dane!")

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
                self.save()
                print("Do zobaczenia!")
                break
            else:
                print("Niepoprawna opcja!")

if __name__ == '__main__':
    Journal().run()