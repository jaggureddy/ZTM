"""
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints
Use timeit() function to measure the running time.

"""


import timeit


def loop():
    i = 0
    while i < 100:
        s = 1 + 1
        i += 1


print(timeit.timeit("loop()", setup="from __main__ import loop"))
