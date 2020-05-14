"""
Define a class named American and its subclass NewYorker.

Hints:
Use class Subclass(ParentClass) to define a subclass.*

"""

class American():
    def __init__(self):
        print("American")

class NewYorker(American):
    def __init__(self):
        print("Newyorker")


ny = NewYorker()
am = American()
