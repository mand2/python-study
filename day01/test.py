class Test:
    __num1: int = 0
    __num2: int = 0

    def __init__(self, num1: int, num2: int):
        if isinstance(num1, int):
            self.__num1 = num1
        if isinstance(num2, int):
            self.__num2 = num2

    def add(self):
        return self.__num1 + self.__num2

    @property
    def num1(self):
        return self.__num1

    @property
    def num2(self):
        return self.__num2


t = Test('1', 1)
print(t.add()) # result : 1
print('num1\t', t.num1, '\nnum2\t', t.num2)
"""
result : 
num1     0
num2     1
"""
