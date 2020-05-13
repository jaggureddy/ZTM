l = []
for i in range(2000, 3001):
    flag = 1
    for j in str(i):
        if int(j) % 2 != 0:
            flag = 0
    if flag == 1:
        l.append(str(i))

print(",".join(l))
