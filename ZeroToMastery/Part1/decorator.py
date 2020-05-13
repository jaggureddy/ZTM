from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000):
        i * 5


user1 = {
    'name': 'Jaggu',
    'valid': True
}


def authenticated(func):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return func(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
