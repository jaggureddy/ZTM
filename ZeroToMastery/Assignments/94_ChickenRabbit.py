"""
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Hints
Use for loop to iterate all possible solutions.
"""


def count(heads, legs):
    for i in range(heads+1):
        j = heads - i
        if 2 * i + 4 * j == legs:
            return i, j
    return 0, 0


print(count(35, 94))
