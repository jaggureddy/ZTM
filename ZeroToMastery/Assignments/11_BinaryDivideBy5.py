l = []

for i in input("").split(","):
    j = int(i, 2)
    if j % 5 == 0:
        l.append(i)

print(" ".join(l))
