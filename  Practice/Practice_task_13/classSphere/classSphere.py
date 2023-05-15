import math


class Sphere:

    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        self.volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return self.volume

    def get_square(self):
        self.square = math.pi * 4 * math.pow(self.radius, 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        self.center = (self.x, self.y, self.z)
        return self.center

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0

    def is_point_inside(self, x0, y0, z0):
        if (math.pow((self.x - x0), 2) + math.pow((self.y - y0), 2)
                + math.pow((self.z - z0), 2) < (math.pow(self.radius, 2))):
            return True
        else:
            return False

print("  Tests:")
s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print("  =============")
print(s0.get_volume()) # 0.523598775598
print("  =============")
print(s0.is_point_inside(0, -1.5, 0)) # False
print("  =============")
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print("  =============")
print(s0.get_radius()) # 1.6