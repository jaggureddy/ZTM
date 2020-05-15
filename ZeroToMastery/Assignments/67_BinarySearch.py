"""
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints
Use if/elif to deal with conditions.

"""

idx = 0


def find(n, li):
    global idx
    start = 0
    l = len(li)
    if l >= 0:
        mid = (start + l) // 2
        if li[mid] == n:
            idx += mid
            return idx
        elif li[mid] < n:
            idx += mid
            return find(n, li[mid:])
        else:
            idx += mid
            return find(n, li[:mid])
    else:
        return -1


print(find(4, [0, 1, 2, 3, 4, 5, 6, 7]))
# print(find(66, [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99, 100]))
