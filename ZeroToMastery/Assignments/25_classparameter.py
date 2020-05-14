"""
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later

"""
class inst:
    name = "Jaggu"

    def __init__(self, name):
        self.name = name

i = inst('K')
print((i.name,'J'))
