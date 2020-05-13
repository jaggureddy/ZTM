my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dup = []

for i in my_list:
    if my_list.count(i) > 1 and i not in dup:
        dup.append(i)

print(dup)