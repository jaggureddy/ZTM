string = input("")

digits = 0;
num = 0;

for i in string:
    if i.isalpha():
       digits = digits+1
    if i.isnumeric():
        num = num + 1

print(digits)
print(num)