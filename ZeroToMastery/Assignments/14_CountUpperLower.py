string = input("")

digits = 0;
num = 0;

for i in string:
    if i.isupper():
       digits = digits+1
    if i.islower():
        num = num + 1

print(digits)
print(num)
