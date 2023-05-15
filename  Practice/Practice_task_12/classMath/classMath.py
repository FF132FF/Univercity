class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


calculation = Math(20, 5)

print(calculation.addition())
print("  ===========")
print(calculation.multiplication())
print("  ===========")
print(calculation.division())
print("  ===========")
print(calculation.subtraction())