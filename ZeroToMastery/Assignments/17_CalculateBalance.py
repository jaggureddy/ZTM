deposit = 0
withdraw = 0

c = []

while True:
    line = input('')
    if line:
        c.append(line)
    else:
        break

for item in c:
    dw = item.split(' ')[0];
    am = float(item.split(' ')[1])
    if dw == 'D' or dw == 'd':
        deposit += am
    if dw == 'W' or dw == 'w':
        withdraw += am

print(deposit-withdraw)
