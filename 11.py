class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"{self.name} - ocena: {self.grade}"

class Journal:
    def __init__(self):
        self.students = []

    def run(self):
        while True:
            print("=== DZIENNIK ===")
            print("1. Dodaj studenta")
            print("2. ....")
            print("x. Zakończenie pracy")

            choise = input("Opcja: ")

            if choise == "1":
                pass
            elif choise == "x" or choise == "X":
                print("Do zobaczenia")
                break
            else:
                print("Niepoprawna opcja!")

if __name__ == '__main__':
    Journal().run()