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