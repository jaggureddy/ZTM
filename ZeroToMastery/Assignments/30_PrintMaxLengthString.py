"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

Hints:
Use len() function to get the length of a string.

"""
def length(i, j):
    if len(i) > len(j):
        print(i)
    elif len(i) < len(j):
        print(j)
    elif len(i) == len(j):
        print(i)
        print(j)


length('adsadasdasdas', 'adsadasdasdas')
