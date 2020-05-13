import math

C, H = 50, 30

i = input("Enter list:")
i_l = i.split(',')
Q_L = []
for D in i_l:
    Q = round(math.sqrt((2 * C * int(D))/H))
    Q_L.append(Q)

print(Q_L)
