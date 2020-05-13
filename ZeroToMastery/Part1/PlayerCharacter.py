class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding(cls, num1, num2):
        return num1 + num2

    def oldest(*args):
        return max(args)

    @staticmethod
    def adding1(num1, num2):
        return num1 + num2


cat1 = Cat('One', 10)
cat2 = Cat('Two', 20)
cat3 = Cat('Three', 30)

print(f"The oldest cat is {Cat.oldest(cat1.age, cat2.age, cat3.age)} years old.")

print(cat1.adding(2, 3))
print(Cat.adding1(2, 3))
