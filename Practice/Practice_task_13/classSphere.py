import math


class Sphere:

    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def getVolume(self):
        self.volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return self.volume

    def getSquare(self):
        self.square = math.pi * 4 * math.pow(self.radius, 2)

    def getRadius(self):
        return self.radius

    def getCenter(self):
        self.center = (self.x, self.y, self.z)
        return self.center

    def setRadius(self, r):
        self.radius = r

    def setCenter(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0

    def isPointInside(self, x0, y0, z0):
        if (math.pow((self.x - x0), 2) + math.pow((self.y - y0), 2)
                + math.pow((self.z - z0), 2) < (math.pow(self.radius, 2))):
            return True
        else:
            return False

print("  Tests:")
s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.getCenter()) # (0.0, 0.0, 0.0)
print("  =============")
print(s0.getVolume()) # 0.523598775598
print("  =============")
print(s0.isPointInside(0, -1.5, 0)) # False
print("  =============")
s0.setRadius(1.6)
print(s0.isPointInside(0, -1.5, 0)) # True
print("  =============")
print(s0.getRadius()) # 1.6