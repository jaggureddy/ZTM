item = int(input('Enter item: '))

fact = 1
i = 1
while i <= item:
    fact = fact * i
    i = i + 1

print(fact)

fact1 = 1
for i1 in range(1, item + 1):
    fact1 = fact1 * i1;

print(fact1)


def short(x): return 1 if x < 1 else x * short(x - 1)


print(short(item))
