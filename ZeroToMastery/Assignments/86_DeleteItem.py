"""
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints
Use list's remove method to delete a value.

"""

li = [12, 24, 35, 24, 88, 120, 155]
for i in li:
    if i == 24:
        li.remove(i)

print(li)
