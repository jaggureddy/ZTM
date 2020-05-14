"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
l = []
for i in range(2000, 3001):
    flag = 1
    for j in str(i):
        if int(j) % 2 != 0:
            flag = 0
    if flag == 1:
        l.append(str(i))

print(",".join(l))
