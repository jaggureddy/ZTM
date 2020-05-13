l = [1,2,3,4,5,6,7,8,9,10]

# for i in l:
#     m.__setitem__(i, i**2)

squaredNumbers = map(lambda x: x**2, l)

print(list(squaredNumbers))
