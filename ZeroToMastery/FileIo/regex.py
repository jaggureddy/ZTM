import re

# pattern = re.compile('this')
# pattern = re.compile(r'([a-zA-Z]).([a])')
# text = 'search inside of this text'
pattern = re.compile(r'(^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
# a = re.search('this', text)
email = 'test@email.com'
a = pattern.search(email)

print(a)

# password = re.compile(r'[a-zA-Z0-9@$%#]{7,}\d')
password = re.compile(r'[a-zA-Z0-9@$%#]{7,}[0,9]')


passw = 'Jaggu@5512'
b = password.fullmatch(passw)

print(b)

# r'(^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
