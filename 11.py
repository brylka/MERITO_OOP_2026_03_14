class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"{self.name} - ocena: {self.grade}"



if __name__ == '__main__':
    student1 = Student("Bartosz", 4)
    print(student1)