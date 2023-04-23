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
        num_good_grades = sum(grade > 5.5 for grade in self.grades)
        percentage_good_grades = num_good_grades / len(self.grades)
        return percentage_good_grades >= 0.75


Pieter = Student("Pieter", [6.0, 7.0, 8.0])
Jimmy = Student("Jimmy", [5.0, 4.0, 3.0])
Jack = Student("Jack", [5.0, 7.0, 8.0])
Timmie = Student("Timmie", [5.0, 10.0, 8.0])
Sandy = Student("Sandy", [9.0, 7.0, 8.0])
Jaqueline = Student("Jaqueline", [5.0, 4.0, 3.0])

print(Jack.calc_average())


class Course:
    def __init__(self, name: str, students: list):
        self.name = name
        self.students = list(students)

    def add_student(self, Student):
        self.students.append(Student)

    def calc_average(self):
        return [student.calc_average() for student in self.students]

    def check_studentBSA(self):
        negative_BSA = []
        for student in self.students:
            if not student.achieve_BSA():
                negative_BSA.append(str(student))
        # breaking up print statement to make it pep8 compliant
        print("The following students did not achieve the BSA: ", +
              (negative_BSA))


Biology = Course("Biology", [Pieter, Jimmy, Jack, Timmie, Sandy, Jaqueline])

# Biology.check_studentBSA()


class Faculty:
    def __init__(self, name: str, courses: list):
        self.name = name
        self.courses = [] if courses is None else courses

    def add_course(self, Course):
        self.courses.append(Course)

    def calc_average(self):
        average = sum(self.courses) / len(self.courses)
        return average

    def get_best_3_grades(self, grades):
        sorted_grades = sorted(grades, reverse=True)
        return sorted_grades[:3]

    def get_excellence(self):
        for course in self.courses:
            print(f"Top 3 students in {course.name}:")
            top_students = sorted(
                course.students,
                # key=lamba needed to sort by value, not by object
                key=lambda x: x.calc_average(),
                reverse=True)[
                :3]
            for i, student in enumerate(top_students):
                print(f"{i+1}. {student.name} ({student.calc_average():.1f})")
            print()


faculty = Faculty("Science", [Biology])


faculty.get_excellence()
faculty.print_top_3_students()
