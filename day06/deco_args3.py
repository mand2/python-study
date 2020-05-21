"""
debugging 하기 쉬운 decorator 만들기
   : a good advisory decorator for debugging
ref: https://www.datacamp.com/community/tutorials/decorators-python
"""


def decorator_passing_arbitrary_arguments(func):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        """THIS IS Wrapper Function !!"""
        print('positional args:', args)
        print('key word args  :', kwargs)
        func(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@decorator_passing_arbitrary_arguments
def func_no_args():
    print('func_no_args')


# bad for debugging. cannot know function itself
print(func_no_args.__name__)  # a_wrapper_accepting_arbitrary_arguments
print(func_no_args.__doc__)  # THIS IS Wrapper Function !!

import functools


def updated_decorator_function(func):
    @functools.wraps(func)
    def updated_wrapper():
        return print(func().upper())  # 대문자로만

    return updated_wrapper


@updated_decorator_function
def updated_func():
    """This is Updated Function"""
    return 'hello there'


updated_func()
print(updated_func.__name__)  # updated_func
print(updated_func.__doc__)  # This is Updated Function

"""
`functools` 를 사용하면 
해당 메서드의 name, doc 을 정확하게 사용할 수 있다.
"""

