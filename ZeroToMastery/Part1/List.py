li = [
    'apple',
    '1',
    True,
    False,
    2.5,
    2
]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

li.append(5+4j)
li.extend(['asdsd'])
li.insert(4, 'asdasddsa')

li.pop()
li.pop(0)
li.remove(True)

print(li)
print(li.count('1'))

li.reverse()
print(li)
print(len(li))

li.clear()
print(li)

print(list(range(1, 100, 2)))