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

    def __str__(self):
        avgRaiting = self.averageRaiting()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avgRaiting}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.coursesAttached = []

    def rateStudent(self, student, course, grade):
        if course in self.coursesAttached and course in student.coursesInProgress:
            student.grades[course] = [grade]

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

