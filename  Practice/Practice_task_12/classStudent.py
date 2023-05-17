class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, changedName, changedAge):
        self.name = changedName
        self.age = changedAge

    def setGroupNumber(self, changedGroupNumber):
        self.groupNumber = changedGroupNumber


egor = Student("Egor", 23, "5В")
ivan = Student("Ivan", 31, "7A")
elizaveta = Student("Elizaveta", 28, "9D")
andrey = Student()
polina = Student()

print(egor.getName())
print(ivan.getAge())
print(elizaveta.getGroupNumber())

print("  ===========")

andrey.setNameAge("Andrey", 20)
andrey.setGroupNumber("11A")
print(andrey.getName())
print(andrey.getAge())
print(andrey.getGroupNumber())

print("  ===========")

polina.setNameAge("Polina", 17)
polina.setGroupNumber("3C")
print(polina.getName())
print(polina.getAge())
print(polina.getGroupNumber())

print("  ===========")

ivan.setNameAge("Alexey", 32)
print(ivan.getName())
print(ivan.getAge())