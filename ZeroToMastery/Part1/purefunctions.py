def mul(li):
    new_li = []
    for item in li:
        new_li.append(item * 2)
    return new_li


print(mul([1, 2, 3]))

my_list = [2, 4, 6]


def mul1(item):
    return item * 2


# map, filter, zip, reduce
# map(function, data)
print(list(map(mul1, [1, 3, 5])))
print(list(map(mul1, my_list)))


def odd(item):
    return item % 2 != 0


print(list(filter(odd, [1, 2, 3])))
print(list(filter(odd, my_list)))

li1 = [1, 2, 3]
li2 = (10, 20, 30)
li3 = {100, 200, 300}

print(list(zip(li1, li2, li3)))

from functools import reduce


def red(acc, item):
    return item + acc


print(reduce(red, li1))
