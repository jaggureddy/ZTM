"""
from time import time

def generator():
    for i in range(10):
        yield i * 2


for item in generator():
    print(item)

g = generator()
print(g)
print(next(g))
next(g)
next(g)
print(next(g))


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i * 5


long_time()
long_time2()
"""


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


special_for([1, 2, 3])


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = self.first
        # this line allows us to use the current number as the starting point for the iteration

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 100)
for i in gen:
    print(i)
