"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.

"""
import math
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return math.pi * self.radius * self.radius


c = Circle(1)
print(c.area())
