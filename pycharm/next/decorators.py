# performance decorator

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}')
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000):
        i * 5


long_time()


# from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result

    return wrapper


@performance
def long_time():
    print('1')
    for i in range(100000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i * 5


long_time()
long_time2()


# Create an @authenticated decorator
# only allows the function to run if user1 has 'valid' set to True

user1 = {'name': 'Sona', 'valid': True}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
