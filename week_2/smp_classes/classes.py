class Student {
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = []

    def addGrade(self, grade: float):
        self.grades.append(grade)

    def calcAverage(self):
        average = sum(self.grades) / len(self.grades)
        return average
}


class Course {
    def __init__(self, name: str, students: list):
        self.name = name
        self.students = []

    def addStudent(self, Student):
        self.students.append(Student)

    def calcAverage(self):
        average = sum(self.students) / len(self.students)
        return average
}


class Faculty {
    def __init__(self, name: str, courses: list):
        self.name = name
        self.courses = []

    def addCourse(self, Course):
        self.courses.append(Course)

    def calcAverage(self):
        average = sum(self.courses) / len(self.courses)
        return average
}
