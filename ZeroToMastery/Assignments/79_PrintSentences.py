"""
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints
Use list[index] notation to get a element from a list.

"""

l1 = ['I', 'You']
l2 = ['Play', 'Love']
l3 = ['Hockey', 'Football']

for i in l1:
    for j in l2:
        for k in l3:
            print(f'{i} {j} {k}')
