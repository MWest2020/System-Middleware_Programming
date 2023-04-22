class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = list(grades)

    def __str__(self):
        return f"{self.name}"

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def get_grades(self):
        print(self.grades)
        return self.grades

    def calc_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def achieve_BSA(self):
        average_grade = self.calc_average()
        return average_grade > 5.5


Pieter = Student("Pieter", [6.0, 7.0, 8.0])
Jimmy = Student("Jimmy", [5.0, 4.0, 3.0])
Jack = Student("Jack", [6.0, 7.0, 8.0])

# Pieter.add_grade(6.0)
print(Pieter.get_grades())
print("Here's the BSA: ", Pieter.achieve_BSA())


class Course:
    def __init__(self, name: str, students: list):
        self.name = name
        self.students = []

    def add_student(self, Student):
        self.students.append(Student)

    def get_students(self):
        for student in self.students:
            print(student.grades)

    # def calc_average(self, students):
    #     average = sum(Student.grades) / len(students)
    #     return average

    def check_studentBSA(self) -> list:
        negative_BSA = []
        for student in self.students:
            if student.achieve_BSA() is False:
                negative_BSA.append(student)
        print("The folowing students did not achieve the BSA:, negative_BSA")
        return negative_BSA


Biology = Course("Biology", [Pieter, Jimmy, Jack])

Biology.add_student(Pieter)
Biology.add_student(Jimmy)
Biology.add_student(Jack)


class Faculty:
    def __init__(self, name: str, courses: list):
        self.name = name
        self.courses = []

    def addCourse(self, Course):
        self.courses.append(Course)

    def calcAverage(self):
        average = sum(self.courses) / len(self.courses)
        return average
