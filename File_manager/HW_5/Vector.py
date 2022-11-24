import random


# author: Kashapova Dilyara

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        try:
            return Vector(self.x + other.x, other.y + self.y)
        except AttributeError:
            print("Второй параметр не является вектором\n")

    def __sub__(self, other):
        try:
            return Vector(self.x - other.x, self.y - other.y)
        except AttributeError:
            print("Второй параметр не является вектором\n")

    def __mul__(self, other):
        try:
            return Vector(self.x * other.x, self.y * other.y)
        except AttributeError:
            print("Второй параметр не является вектором\n")

    def __str__(self):
        return f'({self.x}, {self.y})'


vec1 = Vector(random.randint(-5, 5), random.randint(-5, 5))
vec2 = Vector(random.randint(-5, 5), random.randint(-5, 5))
i = 9

print(f'vec1  {vec1.__str__()}')
print(f'vec2 {vec2.__str__()}')

vec3 = vec1.__add__(i)

print(f'vec1 + vec2 {(vec1 + vec2).__str__()}')
print(f'vec1 - vec2 {(vec1 - vec2).__str__()}')
print(f'vec1 * vec2 {(vec1 * vec2).__str__()}')
