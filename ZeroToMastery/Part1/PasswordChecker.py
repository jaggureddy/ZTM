name = input('what is your name? ')
password = input('what is your password? ')
password_length = len(password)
secret = '*' * password_length
print(f'Hello {name}, Your Password is {secret} and {password_length} letters long')