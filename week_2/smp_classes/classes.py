class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = []

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def calc_average(self):
        average = sum(self.grades) / len(self.grades)
        return average

    def achieve_BSA(self):
        for grade in self.grades:
            if grade < 5.5:
                return False


class Course:
    def __init__(self, name: str, students: list):
        self.name = name
        self.students = []

    def add_student(self, Student):
        self.students.append(Student)

    def calc_average(self):
        average = sum(self.students) / len(self.students)
        return average

    def check_studentBSA(students) -> list:
        negative_BSA = []
        for student in students:
            if student.achieve_BSA() is False:
                negative_BSA.append(student)
        return negative_BSA


class Faculty:
    def __init__(self, name: str, courses: list):
        self.name = name
        self.courses = []

    def addCourse(self, Course):
        self.courses.append(Course)

    def calcAverage(self):
        average = sum(self.courses) / len(self.courses)
        return average
