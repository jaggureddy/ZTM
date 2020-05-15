"""
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints
Use random.sample() to generate a list of random values.

"""

import random

rand = [i for i in range(100, 201) if i % 2 == 0]
print(random.sample(rand, 5))


# resp = random.sample(range(100,201,2),5)
# print(resp)
