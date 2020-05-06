"""
ref: https://www.datacamp.com/community/tutorials/decorators-python
succeed to decorator_test.py
"""


def greeting_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper


def morning():
    return 'good morning!'


decorate = greeting_decorator(morning)
decorate()
print(decorate())  # GOOD MORNING!
