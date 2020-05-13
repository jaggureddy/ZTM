tup = [('Tom', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]

tup.sort(key=lambda x:(x[0],x[1],x[2]))

print(tup)