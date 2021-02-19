from time import time


# Decorators work due to the ability of functions to act like variables, to act like first class citizens in Python
# In short, decorators supercharge our functions, add extra functionality to them

# Also we need to understand the idea of Higher Order Function
# A HOC can be a function that accepts another function:
def greet(func):
    func()
    pass


# Or also a function that returns another function:
def greet2():
    def func():
        return 5

    return func()


# With the HOC ready, a decorator supercharges a function (wraps another function and enhances it)
def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')

    return wrap_func()


@my_decorator
def hello():
    print('hello')


hello


# Practical exercise - Creating a Decorator
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result

    return wrapper()


@performance
def log_time():
    for i in range(1000000):
        i * 5


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
