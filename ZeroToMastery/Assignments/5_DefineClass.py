"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters



"""

class UpperCase():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter Input:")

    def printString(self):
        print(self.str.upper())


strObj = UpperCase()
strObj.getString()
strObj.printString()