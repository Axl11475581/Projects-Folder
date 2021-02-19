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
