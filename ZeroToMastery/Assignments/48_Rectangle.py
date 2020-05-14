"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.

"""


class Rectangle():
    def __init__(self, len, width):
        self.len = len
        self.width = width

    def area(self):
        return self.len * self.width


r = Rectangle(4, 5)
print(r.area())
