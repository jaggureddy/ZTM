"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

"""
import math

c = []

while True:
    line = input('')
    if line:
        c.append(line)
    else:
        break

x, y = 0, 0

prev = ''

for i in c:
    stage = i.split(' ')[0]
    dista = int(i.split(' ')[1])
    if prev == '' and stage == 'UP':
        x += dista
        prev = 'UP'
    if prev == 'UP' and stage == 'DOWN':
        x -= dista
        prev = 'DOWN'
    if prev == 'DOWN' and stage == 'LEFT':
        y -= dista
        prev = 'LEFT'
    if prev == 'LEFT' and stage == 'RIGHT':
        y += dista
        prev = 'RIGHT'

print(x, y)
print(round(math.sqrt(x**2 + y**2)))
