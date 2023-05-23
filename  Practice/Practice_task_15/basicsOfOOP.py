class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finishedCourses = []
        self.coursesInProgress = []
        self.grades = {}

    def addCourse(self, courseName):
        self.finishedCourses.append(courseName)

    def rateLecturer(self, lecturer, course, grade):
        if course in lecturer.coursesAttached and (course in self.coursesInProgress or course in self.finishedCourses):
            lecturer.grades[course] = [grade]

    def averageRating(self):
        sum = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                count += 1
        if count == 0:
            return "Не оценен"
        return round(sum / count, 3)

    def __str__(self):
        avgRating = self.averageRating()
        coursesInProgress = ', '.join(self.coursesInProgress)
        finishedCourses = ', '.join(self.finishedCourses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avgRating}" \
               f"\nКурсы в процессе изучения: {coursesInProgress}\nЗавершенные курсы: {finishedCourses}"

    def __int__(self):
        return len(self.grades)

    def __float__(self):
        sum = 0
        if len(self.grades) != 0:
            for grades in self.grades.values():
                for grade in grades:
                    sum += grade
            avr = sum / len(self.grades)
        return avr

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
        z = complex(mx, mn)
        return z

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        student.grades[course] = [grade]


    def addCourse(self, course):
        self.coursesAttached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.coursesAttached = []

    def averageRaiting(self):
        sum = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                count += 1
        if count == 0:
            return "Не оценен"
        return round(sum / count, 3)

    def __int__(self):
        return len(self.grades)

    def __float__(self):
        sum = 0
        if len(self.grades) != 0:
            for grades in self.grades.values():
                for grade in grades:
                    sum += grade
            avr = sum / len(self.grades)
        return avr

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
        z = complex(mx, mn)
        return z
    def __str__(self):
        avgRaiting = self.averageRaiting()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avgRaiting}"



class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and ((course in student.coursesInProgress)
                                               or (course in student.finishedCourses)):
            student.grades[course] = [grade]

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



firstStudent = Student("Andrey", "Andrey", "male")
secondStudent = Student("Pavel", "Pavel", "male")

firstReviewer = Reviewer("Ilya", "Ilya")
firstReviewer.addCourse("python")
firstReviewer.addCourse("c++")
firstReviewer.addCourse("JS")
firstStudent.addCourse("python")
firstStudent.addCourse("c++")
firstStudent.addCourse("JS")
secondStudent.addCourse("python")
secondStudent.addCourse("c++")
firstReviewer.rateStudent(secondStudent, "python", 3)
firstReviewer.rateStudent(secondStudent, "c++", 8)
firstReviewer.rateStudent(firstStudent, "python", 7)
firstReviewer.rateStudent(firstStudent, "c++", 7)
firstReviewer.rateStudent(firstStudent, "JS", 9)

firstLecturer = Lecturer("Alexey", "Alexey")
firstLecturer.addCourse("python")
firstLecturer.addCourse("c++")
firstLecturer.addCourse("JS")

firstStudent.rateLecturer(firstLecturer, "JS", 9)
firstStudent.rateLecturer(firstLecturer, "c++", 6)
firstStudent.rateLecturer(firstLecturer, "python", 8)
secondStudent.rateLecturer(firstLecturer, "python", 3)
secondStudent.rateLecturer(firstLecturer, "c++", 9)






print(firstStudent.__str__())
print(firstStudent.__int__())
print(firstStudent.__bool__())
print(firstStudent.__complex__())
print(firstStudent.__float__())
print("  ===========")
print(secondStudent.__str__())
print(secondStudent.__int__())
print(secondStudent.__bool__())
print(secondStudent.__complex__())
print(secondStudent.__float__())
print("  ===========")
print(firstLecturer.__str__())
print(firstLecturer.__int__())
print(firstLecturer.__bool__())
print(firstLecturer.__complex__())
print(firstLecturer.__float__())