item = int(input("Enter number: "))

d = {}

for i in range(1, item + 1):
    d[i] = i * i

print(d)


ans = {i: i*i for i in range(1, item+1)}
print(ans)

