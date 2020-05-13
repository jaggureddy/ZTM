# my_file = open('C:\\Users\\JR0544\\Desktop\\Scanned Receiving\\DB Urls - Copy.txt')
#
# print(my_file.readlines())
# my_file.seek(0)
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.read())
# my_file.close()
# try:
#     with open('C:\\Users\\JR0544\\Desktop\\Scanned Receiving\\DB Urls - Copy1.txt', mode='r+') as my_file1:
#         text = my_file1.write('test input: test')
#         print(my_file.readlines())
# except FileNotFoundError as err:
#     print('File not found')
#     raise err
from translate import Translator
try:
    with open('C:\\Users\\JR0544\\Desktop\\Scanned Receiving\\DB Urls - Copy.txt', mode='r') as my_file:
        text = my_file.read()
        translator = Translator(to_lang='ja')
        t = translator.translate(text)
        print(t)
except Exception as err:
    raise err

