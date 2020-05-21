"""
accepting arguments in Decorator functions
ref: https://www.datacamp.com/community/tutorials/decorators-python

learn how to manage arguments - called `*args`
"""


def decorator_passing_arbitrary_arguments(func):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('positional args:', args)
        print('key word args  :', kwargs)
        func(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments


@decorator_passing_arbitrary_arguments
def func_no_args():
    print('func_no_args')


@decorator_passing_arbitrary_arguments
def func_args(a, b, c):
    print('func_args', a, b, c)


@decorator_passing_arbitrary_arguments
def func_kwargs(**kwargs):
    print('func_kwargs', kwargs)


func_no_args()
"""
positional args: ()
key word args  : {}
func_no_args  # func(*args, **kwargs)이 호출된 결과
"""

func_args(1, 5, 29)
"""
positional args: (1, 5, 29)
key word args  : {}
func_args 1 5 29  # func(*args, **kwargs)이 호출된 결과
"""

func_kwargs(age=29, name='hi')
"""
positional args: ()
key word args  : {'age': 29, 'name': 'hi'}
func_kwargs {'age': 29, 'name': 'hi'}  # func(*args, **kwargs)이 호출된 결과
"""


@decorator_passing_arbitrary_arguments
def func_mixed(*args, **kwargs):
    print('mixed\n', args, kwargs)


""" ############### 응용 ############## """
# args kwargs 순서대로 와야하기 때문에 bike 맨 뒤에 올 수 X
func_mixed('tree', 'sky', 'bike', age=29, name='hi')

"""
positional args: ('tree', 'sky', 'bike')
key word args  : {'age': 29, 'name': 'hi'}
mixed
 ('tree', 'sky', 'bike') {'age': 29, 'name': 'hi'}
"""

