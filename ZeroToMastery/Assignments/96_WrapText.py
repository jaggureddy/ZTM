"""
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
Hints
Use wrap function of textwrap module

"""

import textwrap

s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
print(textwrap.fill(s, 4))
