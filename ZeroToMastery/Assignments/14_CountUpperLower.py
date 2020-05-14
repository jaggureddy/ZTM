"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
string = input("")

digits = 0;
num = 0;

for i in string:
    if i.isupper():
       digits = digits+1
    if i.islower():
        num = num + 1

print(digits)
print(num)
