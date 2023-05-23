class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finishedCourses = []
        self.coursesInProgress = []
        self.grades = {}

    def addCourse(self, courseName):
        if courseName in self.coursesInProgress and self.grades[courseName] != []:
            self.finishedCourses.append(courseName)
        else:
            self.coursesInProgress.append(courseName)


    def rateLecturer(self, lecturer, course, grade):
        if course in lecturer.coursesAttached and (course in self.coursesInProgress or course in self.finishedCourses):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]

    def averageRating(self):
        sum = 0
        count = 0
        for grade in self.grades.values():
            count += len(grade)
            for element in grade:
                sum += element
        if count == 0:
            return "Не оценен"
        return round(sum / count, 2)

    def __int__(self):
        count = 0
        for grade in self.grades.values():
            count += len(grade)
        return count

    def __float__(self):
        return self.averageRating()

    def __bool__(self):
        if len(self.grades) % 2 == 1:
            return True
        else:
            return False

    def __complex__(self):
        mn = 11.0
        mx = -1.0
        for grades in self.grades.values():
            for grade in grades:
                if grade > mx:
                    mx = grade
                if grade < mn:
                    mn = grade
        if mn == 11.0 and mx == -1.0:
            return "Не оценен"
        z = complex(mx, mn)
        return z

    def __str__(self):
        avgRating = self.averageRating()
        coursesInProgress = ', '.join(self.coursesInProgress)
        finishedCourses = ', '.join(self.finishedCourses)
        return f"   Имя: {self.name}\n    Фамилия: {self.surname}\n    Средняя оценка за домашние задания: {avgRating}"\
               f"\n    Курсы в процессе изучения: {coursesInProgress}\n    Завершенные курсы: {finishedCourses}"

    def __name__(self):
        return "Student"

    def __dict__(self):
        attributeDict = {}
        attributeDict["name"] = self.name
        attributeDict["surname"] = self.surname
        attributeDict["gender"] = self.gender
        attributeDict["finishedCourses"] = self.finishedCourses
        attributeDict["coursesInProgress"] = self.coursesInProgress
        attributeDict["grades"] = self.grades
        return attributeDict

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and (
                course in student.coursesInProgress or course in student.finishedCourses):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def addCourse(self, course):
        self.coursesAttached.append(course)

    def __name__(self):
        return "Mentor"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.coursesAttached = []

    def averageRating(self):
        sum = 0
        count = 0
        for grade in self.grades.values():
            count += len(grade)
            for element in grade:
                sum += element
        if count == 0:
            return "Не оценен"
        return round(sum / count, 2)

    def __int__(self):
        count = 0
        for grade in self.grades.values():
            count += len(grade)
        return count

    def __float__(self):
        return self.averageRating()

    def __bool__(self):
        if len(self.grades) % 2 == 1:
            return True
        else:
            return False

    def __complex__(self):
        mn = 11.0
        mx = -1.0
        for grades in self.grades.values():
            for grade in grades:
                if grade > mx:
                    mx = grade
                if grade < mn:
                    mn = grade
        if mn == 11.0 and mx == -1.0:
            return "Не оценен"
        z = complex(mx, mn)
        return z
    def __str__(self):
        avgRating = self.averageRating()
        return f"   Имя: {self.name}\n    Фамилия: {self.surname}\n    Курсы: {', '.join(self.coursesAttached)}" \
               f"\n    Средняя оценка за лекции: {avgRating}"

    def __name__(self):
        return "Lecturer"

    def __dict__(self):
        attributeDict = {}
        attributeDict["name"] = self.name
        attributeDict["surname"] = self.surname
        attributeDict["grades"] = self.grades
        attributeDict["coursesAttached"] = self.coursesAttached
        return attributeDict


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and course in student.coursesInProgress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f"   Имя: {self.name}\n    Фамилия: {self.surname}\n    Курсы: {', '.join(self.coursesAttached)}"

    def __name__(self):
        return "Reviewer"
    def __dict__(self):
        attributeDict = {}
        attributeDict["name"] = self.name
        attributeDict["surname"] = self.surname
        attributeDict["coursesAttached"] = self.coursesAttached
        return attributeDict


def avgGradeStudentsOfCourse(studentsList, courseName):
    grades = []
    for student in studentsList:
        if courseName in student.grades:
            grades.extend(student.grades[courseName])
    if grades:
        return sum(grades) / len(grades)
    else:
        return

def avgGradeLecturersOfCourse(lecturersList, courseName):
    grades = []
    for lecturer in lecturersList:
        if courseName in lecturer.grades:
            grades.extend(lecturer.grades[courseName])
    if grades:
        return sum(grades) / len(grades)
    else:
        return


firstStudent = Student("Andrey", "FFFFFF", "male")
firstStudent.addCourse("python")
firstStudent.addCourse("c++")
firstStudent.addCourse("JS")

secondStudent = Student("Pavel", "DDDDDD", "male")
secondStudent.addCourse("python")
secondStudent.addCourse("c++")

firstReviewer = Reviewer("Ilya", "SSSSSS")
firstReviewer.addCourse("python")
firstReviewer.addCourse("c++")
firstReviewer.addCourse("JS")

secondReviewer = Reviewer("Dmitriy", "HHHHHH")
secondReviewer.addCourse("c++")
secondReviewer.addCourse("python")

firstLecturer = Lecturer("Alexey", "GGGGGG")
firstLecturer.addCourse("python")
firstLecturer.addCourse("c++")
firstLecturer.addCourse("JS")

secondLecturer = Lecturer("Sergey", "AAAAAA")
secondLecturer.addCourse("c++")

firstReviewer.rateStudent(firstStudent, "python", 6)
firstReviewer.rateStudent(firstStudent, "c++", 7)
firstReviewer.rateStudent(firstStudent, "JS", 9)
secondReviewer.rateStudent(firstStudent, "c++", 8)
secondReviewer.rateStudent(firstStudent, "python", 7)

firstReviewer.rateStudent(secondStudent, "python", 3)
firstReviewer.rateStudent(secondStudent, "c++", 9)
secondReviewer.rateStudent(secondStudent, "c++", 10)
secondReviewer.rateStudent(secondStudent, "python", 4)

firstStudent.rateLecturer(firstLecturer, "JS", 9)
firstStudent.rateLecturer(firstLecturer, "c++", 2)
firstStudent.rateLecturer(firstLecturer, "python", 8)
secondStudent.rateLecturer(firstLecturer, "python", 6)
secondStudent.rateLecturer(firstLecturer, "c++", 9)

firstStudent.rateLecturer(secondLecturer, "c++", 10)
secondStudent.rateLecturer(secondLecturer, "c++", 9)


print("\n    ======================================================================================================="
      "=======    \n")
print("Метод student.__name__() выводит имя класса:\n   ", firstStudent.__name__())
print("\nМетод student.__dict__() выводит словарь с атрибутами класса:\n   ", firstStudent.__dict__())
print("\nМетод student.__str__() выводит основную информацию об экземпляре класса Student:\n", firstStudent.__str__())
print("\nМетод student.__int__() выводит общее количество оценок по всем курсам экзмепляра класса Student:\n   ",
      firstStudent.__int__())
print("\nМетод student.__bool__() выводит True, если общее количество оценок по всем курсам экзмепляра класса Student не "
      "четное, и False, если четное:\n   ", firstStudent.__bool__())
print("\nМетод student.__complex__() приводит общее количество оценок по всем курсам экзмепляра класса Student к "
      "комплексному типу:\n   ", firstStudent.__complex__())
print("\nМетод student.__float__() выводит среднюю оценку за домашние задания по всем курсам экзмепляра класса Student "
      ":\n   ", firstStudent.__float__())
print("\n    ======================================================================================================="
      "=======    \n")
print("Метод student.__name__() выводит имя класса:\n   ", secondStudent.__name__())
print("\nМетод student.__dict__() выводит словарь с атрибутами класса:\n   ", secondStudent.__dict__())
print("\nМетод student.__str__() выводит основную информацию об экземпляре класса Student:\n", secondStudent.__str__())
print("\nМетод student.__int__() выводит общее количество оценок по всем курсам экзмепляра класса Student:\n   ",
      secondStudent.__int__())
print("\nМетод student.__bool__() выводит True, если общее количество оценок по всем курсам экзмепляра класса Student не "
      "четное, и False, если четное:\n   ", secondStudent.__bool__())
print("\nМетод student.__complex__() приводит общее количество оценок по всем курсам экзмепляра класса Student к "
      "комплексному типу:\n   ", secondStudent.__complex__())
print("\nМетод student.__float__() выводит среднюю оценку за домашние задания по всем курсам экзмепляра класса Student "
      ":\n   ", secondStudent.__float__())
print("\n    ======================================================================================================="
      "=======    \n")
print("Метод lecturer.__name__() выводит имя класса:\n   ", firstLecturer.__name__())
print("\nМетод lecturer.__dict__() выводит словарь с атрибутами класса:\n   ", firstLecturer.__dict__())
print("\nМетод lecturer.__str__() выводит основную информацию об экземпляре класса Lecturer:\n", firstLecturer.__str__())
print("\nМетод lecturer.__int__() выводит общее количество оценок по всем курсам экзмепляра класса Lecturer:\n   ",
      firstLecturer.__int__())
print("\nМетод lecturer.__bool__() выводит True, если общее количество оценок по всем курсам экзмепляра класса Lecturer "
      "не четное, и False, если четное:\n   ", firstLecturer.__bool__())
print("\nМетод lecturer.__complex__() приводит общее количество оценок по всем курсам экзмепляра класса Lecturer к "
      "комплексному типу:\n   ", firstLecturer.__complex__())
print("\nМетод lecturer.__float__() выводит среднюю оценку за домашние задания по всем курсам экзмепляра класса Lecturer "
      ":\n   ", firstLecturer.__float__())
print("\n    ======================================================================================================="
      "=======    \n")
print("Метод lecturer.__name__() выводит имя класса:\n   ", secondLecturer.__name__())
print("\nМетод lecturer.__dict__() выводит словарь с атрибутами класса:\n   ", secondLecturer.__dict__())
print("\nМетод lecturer.__str__() выводит основную информацию об экземпляре класса Lecturer:\n", secondLecturer.__str__())
print("\nМетод lecturer.__int__() выводит общее количество оценок по всем курсам экзмепляра класса Lecturer:\n   ",
      secondLecturer.__int__())
print("\nМетод lecturer.__bool__() выводит True, если общее количество оценок по всем курсам экзмепляра класса Lecturer "
      "не четное, и False, если четное:\n   ", secondLecturer.__bool__())
print("\nМетод lecturer.__complex__() приводит общее количество оценок по всем курсам экзмепляра класса Lecturer к "
      "комплексному типу:\n   ", secondLecturer.__complex__())
print("\nМетод lecturer.__float__() выводит среднюю оценку за домашние задания по всем курсам экзмепляра класса Lecturer "
      ":\n   ", secondLecturer.__float__())
print("\n    ======================================================================================================="
      "=======    \n")
print("Метод reviewer.__name__() выводит имя класса:\n    ", firstReviewer.__name__())
print("\nМетод reviewer.__dict__() выводит словарь с атрибутами класса:\n   ", firstReviewer.__dict__())
print("\nМетод reviewer.__str__() выводит основную информацию об экземпляре класса Reviewer:\n", firstReviewer.__str__())
print("\n    ======================================================================================================="
      "=======    \n")
print("Метод reviewer.__name__() выводит имя класса:\n   ", secondReviewer.__name__())
print("\nМетод reviewer.__dict__() выводит словарь с атрибутами класса:\n   ", secondReviewer.__dict__())
print("\nМетод reviewer.__str__() выводит основную информацию об экземпляре класса Reviewer:\n", secondReviewer.__str__())
print("\n    ======================================================================================================="
      "=======    \n")

studentList = [firstStudent, secondStudent]
lecturerList = [firstLecturer, secondLecturer]

print("Пример работы метода avgGradeStudentOfCouse, который высчитывает среднюю оценку за домашнее задание по всем "
      "студентам в рамках конкретного курса: \n")
print("    Средняя оценка за домашнее задание по всем студентам в рамках конкретного курса ==python== :",
      avgGradeStudentsOfCourse(studentList, "python"))
print("    Средняя оценка за домашнее задание по всем студентам в рамках конкретного курса ==JS== :",
      avgGradeStudentsOfCourse(studentList, "JS"))
print("    Средняя оценка за домашнее задание по всем студентам в рамках конкретного курса ==c++== :",
      avgGradeStudentsOfCourse(studentList, "c++"))
print("\n    ======================================================================================================="
      "=======    \n")
print("Пример работы метода avgGradeLecturerOfCouse, который высчитывает среднюю оценку за лекции всех лекторов в "
      "рамках конкретного курса: \n")
print("    Средняя оценка за лекции всех лекторов в рамках конкретного курса ==python== :", avgGradeLecturersOfCourse(lecturerList, "python"))
print("    Средняя оценка за лекции всех лекторов в рамках конкретного курса ==JS== :", avgGradeLecturersOfCourse(lecturerList, "JS"))
print("    Средняя оценка за лекции всех лекторов в рамках конкретного курса ==c++== :", avgGradeLecturersOfCourse(lecturerList, "c++"))
print("\n    ======================================================================================================="
      "=======    \n")