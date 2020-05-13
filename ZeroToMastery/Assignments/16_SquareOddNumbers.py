# l = input('').split(',')
# r = []
# for item in l:
#     if int(item) % 2 != 0:
#         r.append(int(item) * int(item))
#
# print(r)


lst = [str(int(item)**2) for item in input('').split(',') if int(item) % 2]

print(",".join(lst))
