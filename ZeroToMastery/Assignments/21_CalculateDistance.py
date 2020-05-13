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
