items = input("Enter List:")
l = []

for i in items.replace(',', ''):
    l.append(i)

lst = items.split(',')
tpl = tuple(lst)

print(lst)
print(tpl)
