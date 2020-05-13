c = sorted(list(set(input('').split(' '))))


for i in c:
    print(f'{i} : {c.count(i)}')
