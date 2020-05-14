"""
Define a custom exception class which takes a string message as attribute.

Hints
To define a custom exception, we need to define a class inherited from Exception.

"""


class CustomExc(Exception):
    def __init__(self, str):
        self.str = str


num = int(input())

try:
    if num < 10:
        raise CustomExc("Input is less than 10")
    elif num > 10:
        raise CustomExc("Input is grater than 10")
except CustomExc as ce:
    print("The error raised: " + ce.str)
