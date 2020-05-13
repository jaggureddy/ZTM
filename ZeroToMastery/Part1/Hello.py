# name = input("what is your name?")
# print("Hello "+name)
from Part2.utility import getName, getPhone
# import pyjokes
from collections import Counter, defaultdict, OrderedDict

# print(getName())
# print(getPhone())
# print(__name__)
# print(random.randint(2, 6))

# print(pyjokes.get_joke())

li = [1, 2, 3, 4, 5, 6, 7, 7]

# print(Counter(li))

print(any(li))


dictionary = defaultdict(lambda: 0, {
    'a': 1,
    'b': 2
})

print(dictionary['C'])
