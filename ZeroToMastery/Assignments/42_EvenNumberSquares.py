l = [1,2,3,4,5,6,7,8,9,10]
m={}
for i in l:
    if i % 2 == 0:
        m.__setitem__(i, i**2)

print(m)
