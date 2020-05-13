for item in 'Jaggu':
    print(item)
print(item)
for item in [1, 2, 3, 4, 5]:
    print(item)
print(item)
for item in ('a', 'b', 'c', 'd', 'e'):
    print(item)
print(item)

my_list = {
        'a': [1, 2, 3],
        'b': 'Hello',
        'c': True
}

for item in my_list:
    print(item)

for item in my_list.items():
    print(item)

for item in my_list.values():
    print(item)

for item in my_list.keys():
    print(item)

for k, v in my_list.items():
    print(k, v)

for item in my_list.items():
    key, value = item
    print(key, value)

