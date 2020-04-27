"""
ref: https://www.datacamp.com/community/tutorials/decorators-python
get-to-know Decorators
Decorators are usually called before the definition of a function you want to decorate.
Functions in Python are first class citizens.
"""


# 1. assigning functions to Variables
def plus_one(number: int) -> int:
    return number + 1


add_one = plus_one  # do not use parenthesis when call the function
add_one(10)  # : 11


# 2. Defining Functions Inside other Functions
def plus_two(number: int) -> int:
    def add_two(num: int) -> int:
        return num + 2

    return add_two(number)


plus_two(1725)  # : 1727


# 3. Passing Functions as Arguments to other Functions
def plus_three(number: int) -> int:
    return number + 3


def call_plus_three(func: int) -> int:
    number_to_add = 50
    return func(number_to_add)


"""
comment of # 3
first, call `call_plus_three`
then, it call func named 'plus_three' with parameter (number: 50)
last, in plus_three, it returns 58 .
"""
call_plus_three(plus_three)  # : 53


# 4. Functions Returning other Functions
def get_upset():
    def angry() -> str:
        return "NOPE!"

    return angry


i_said = get_upset
i_said()  # <function get_upset.<locals>.angry at 0x00000200D915BD38>
u_said = get_upset()
u_said()  # NOPE!


"""
comment of # 4 : concept of Closure
the function `angry` is nested in `get_upset`
if want to get str of `angry()`, need to call get_upset and then call the function again.
so that we get different result between i_said and u_said. 

    i_said: get_upset is assigned. If do `i_said()`, this means call `get_upset()` which returns angry. not angry()
    u_said: get_upset() is assigned, meaning calling angry. If do `u_said`, this means call `angry()`
"""


def get_better():
    msg = 'GOOD!'

    def feelings():
        print(msg)
    return feelings


i_got = get_better()

i_got()  # GOOD!
i_got()  # GOOD!
i_got()  # GOOD!

print(i_got)  # <function get_better.<locals>.feelings at 0x000001B901F9BF78>

print(dir(i_got))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
# '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__']

print(i_got.__closure__)  # (<cell at 0x0000018095AAC738: str object at 0x00000180979619F0>,)  # type: tuple

print(i_got.__closure__[0])  # <cell at 0x00000242BEC6C738: str object at 0x00000242BEF51A30>

print(dir(i_got.__closure__[0]))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']

print(i_got.__closure__[0].cell_contents)  # GOOD!

"""
`get_better`라는 함수를 한번 호출 + `i_got`에 할당
이 때 `msg`가 메모리에 할당됨. 
`i_got`의 __closure__[0].cell_contents 라는 속성? 에 할당되기 때문에 
함수 외부에서 i_got() 을 여러번 하더라도 `feelings()` 호출 가능-
"""


