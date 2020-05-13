# lambda param: action(param)

my_list = [5, 4, 3]

# print(list(map(lambda item: item**2, my_list)))

a = [(0, 2), (9, 9), (4, 3), (10, -1)]
a.sort(key=lambda x: x[1], reverse=True)
# print(a)

# list, set, dictionary comprehensions

li = [num**2 for num in range(0, 20) if num % 2 == 0]

print(li)

s_d = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in s_d.items() if v % 2 == 0}
print(my_dict)

