"""

print((5 + 4) * 10 / 2)  # 45

print(((5 + 4) * 10) / 2)  # 45

print((5 + 4) * (10 / 2))  # 45

print(5 + (4 * 10) / 2)  # 25

print(5 + 4 * 10 // 2)  # 25

counter = 0

counter += 1  # 1
counter += 1  # 2
counter += 1  # 3
counter += 1  # 4
counter -= 1  # 3
counter *= 2  # 6
print(counter)

print("Hello {}, your balance is {}.".format("Cindy", 50))
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")

python = 'I am PYTHON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])

new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

print(basket[1][1][0])

basket = ["Banana", "Apples", "Oranges", "Blueberries"];

basket.remove("Banana")
basket.remove("Blueberries")  # basket.pop()
basket.append("Kiwi")
basket.insert(0, 'Apples')
print(basket.count("Apples"))
basket.clear()

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)

print(sorted(friends))

user_profile = {
    'age': 29,
    'username': 'Jaggu6010',
    'weapons': ['a', 'b', 'c'],
    'is_active': True,
    'clan': 'India'
}
print(user_profile.keys())

user_profile['weapons'].append('d')
print(user_profile)

user_profile.update({'is_banned': False})
print(user_profile)

user_profile['is_banned'] = True
print(user_profile)

user2 = user_profile.copy()
user2.update({'age': 35, 'username': 'Jaggu5512'})
print(user2)

school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
#
# attendance_list = set(attendance_list)
#
# print(attendance_list)
print(school.difference(attendance_list))

# counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum= 0
for item in my_list:
    sum += item
print(sum)


def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()

def highest_even(li):
    for item in li:
        highest = item
        if item % 2 == 0 and highest >= item:
            highest = item
        return highest


print(highest_even([10, 2, 3, 4, 8, 11]))



def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 1, 2, 3, 4, 8]))



class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Jaggu(Cat):
    def sing(self, sounds):
        return f'{sounds}'


Si = Simon('Simon', 10)
Sa = Sally('Sally', 20)
Ja = Jaggu('Jaggu', 30)

my_cats = [Si, Sa, Ja]

pets = Pets(my_cats)

pets.walk()

from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capital(item):
    return item.upper()


print(list(map(capital, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))
scores = [73, 20, 65, 19, 76, 100, 88]


def score(item):
    return item > 50


print(list(filter(score, scores)))


def combine(acc, item):
    return acc + item


print(reduce(combine, (my_numbers+scores)))


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)


duplicates = {value for value in some_list if some_list.count(value) > 1}

print(duplicates)

"""


def checkDriverAge(age=0):
    try:
        if int(age) < 18:
            return 'Sorry, you are too young to drive this car. Powering off'
        elif int(age) > 18:
            return 'Powering On. Enjoy the ride!'
        elif int(age) == 18:
            return 'Congratulations on your first year of driving. Enjoy the ride!'
    except ValueError as err:
        return err

