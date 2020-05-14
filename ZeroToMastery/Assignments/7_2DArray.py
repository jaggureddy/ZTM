"""
_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


"""

X = int(input("Enter X:"))
Y = int(input("Enter Y:"))

l = []

for i in range(0, X):
    temp_l = []
    for j in range(0, Y):
        temp_l.append(i * j)
    l.append(temp_l)

print(l)
