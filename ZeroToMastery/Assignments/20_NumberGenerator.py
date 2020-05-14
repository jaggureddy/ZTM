
"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use class, function and comprehension.
"""
class gene:
    def gen(self, n):
        for i in range(n + 1):
            if i % 7 == 0:
                yield i


n = int(input(''))
for num in gene().gen(n):
    print(num)
