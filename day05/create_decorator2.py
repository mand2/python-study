"""
ref: https://www.datacamp.com/community/tutorials/decorators-python
application of create_decorator1.py
succeed to decorator_test.py

advantages of using these type:
    - don't have to assign decorator_function
    - just put @decorator to what-you-want-to-use function
    - and just call the what-you-want-to-use function !
"""


def greeting_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper


@greeting_decorator
def evening():
    return 'good evening!'


print(evening())  # GOOD EVENING!
