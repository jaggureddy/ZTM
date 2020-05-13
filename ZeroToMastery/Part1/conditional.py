is_old = True
is_license = False
a = 5

if is_old:
    print("You are old")
elif is_license:
    print("YOur licence")
else:
    print("You are not old")

if is_license:
    print("Your licence")

if a < 5:
    print('a<5')
elif a == 5:
    print('a=5')
else:
    print("a>5")

if is_old and is_license:
    print('old enough and can drive')
else:
    print('cant drive')


print(bool(''))
print(bool(0))

username = 'Jaggu'
password = 'Jaggu'

# if username and password:
#     print('Truth')
# else:
#     print('False')

print('Truth') if username and password else print('False')

is_magician = False
is_expert = True

# check if magician and expert
if is_magician and is_expert:
    print("you are a master magician")
# check if magician but not expert
elif is_magician and not is_expert:
    print('you are getting there')
# if you are not a magician
elif not is_magician:
    print('you need magical powers')
else:
    print('you are not good')

