picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
"""
# for i in range(len(picture)):
#     for j in range(len(picture[i])):
#         if picture[i][j] == 0:
#             picture[i][j] = ' '
#         if picture[i][j] == 1:
#             picture[i][j] = '*'
#
# for i in range(len(picture)):
#     print(picture[i])

"""
for i in picture:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')  # change default end line
    print('')  # need a new line after every row

"""
# for image in picture:
#     for pixel in image:
#         if pixel:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')
"""