X = int(input("Enter X:"))
Y = int(input("Enter Y:"))

l = []

for i in range(0, X):
    temp_l = []
    for j in range(0, Y):
        temp_l.append(i * j)
    l.append(temp_l)

print(l)
