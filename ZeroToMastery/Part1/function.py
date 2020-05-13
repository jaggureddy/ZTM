def hello(name='test', emoji='angry'):
    print(f'hello {name} {emoji}')


# positional arguments
hello('Jaggu', '')

# Keyword arguments
hello(emoji='asdada', name='Jaggu')

# Default arguments
hello()
hello('test1')


# *args **kwargs
def super_func(*args):
    print(*args)
    print(args)
    return sum(args)


print(super_func(1, 2, 3, 4))


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(kwargs.values())


print(func(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: parameters, *args, default parameters, **kwargs
# start with local, parent local, Global, built in python functions,

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

x = int(5)
print(x)
