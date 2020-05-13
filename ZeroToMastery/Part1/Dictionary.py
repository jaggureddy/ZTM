dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['a'])

dict2 = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}
print(dict2['a'][2])

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'c': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Hello',
        'c': True
    }
]

print(my_list[1]['a'][2])

print('Hello' in dict2.values())

print(dict2.keys())
print(dict2.values())
print(dict2.items())