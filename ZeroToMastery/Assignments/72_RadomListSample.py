"""
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints
Use random.sample() to generate a list of random values.

"""

import random

rand = [i for i in range(100, 201)]
print(random.sample(rand, 5))
