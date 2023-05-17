class Car:
    def __init__(self, color="Black", type="Sedan", year="2020"):
        self.color = color
        self.type = type
        self.year = year

    def startCar(self):
        return "Автомобиль заведен"

    def shutdownCar(self):
        return "Автомобиль заглушен"

    def assignmentYear(self, assignedYear):
        self.year = assignedYear

    def assignmentType(self, assignedType):
        self.type = assignedType

    def assignmentColor(self, assignedColor):
        self.color = assignedColor

    def getInfo(self):
        print("Year: ", self.year)
        print("Type: ", self.type)
        print("Color: ", self.color)


firstCar = Car()
secondCar = Car("White", "Sedan", 2015)

print(secondCar.startCar())
print(secondCar.shutdownCar())
print("  ===========")

firstCar.assignmentYear(2023)
firstCar.assignmentType("Coupe")
firstCar.assignmentColor("Blue")
firstCar.getInfo()