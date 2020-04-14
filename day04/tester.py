from day04.laptop import Laptop, MyException

laptop = Laptop()
print(laptop.dict())  # {'keyboard': False, 'display': True, 'width': 0, 'height': 0}

laptop.width = True
laptop.keyboard = True
print('set', laptop.dict())  # set {'keyboard': True, 'display': True, 'width': True, 'height': 0}

print('------- exception -------')
try:
    laptop.check()  # True or False -> exception
except MyException as e:
    print(e.get_message())  # type err
print('------- exception -------')


class Test:
    def __init__(self):
        self.__test_laptop = None

    def laptop(self, my_laptop):
        self.__test_laptop = my_laptop
        return self

    def get_laptop(self):
        return self.__test_laptop

    def check(self):
        try:
            if self.__test_laptop is not None \
                    and isinstance(self.__test_laptop, Laptop):
                return self.__test_laptop.check()  # 여기서 err raise 나올 수 있다. -(1)
            elif not isinstance(self.__test_laptop, Laptop):
                raise MyException('laptop 자체 타입에러')
            else:
                raise MyException('required field - laptop')
        except MyException:  # 그래서 laptop.check() 일 때 발생한 exception을 그대로 가져가고자 한다면
            raise            # raise만 단독으로 쓰면 됨. -(2)


print('----- again -----')
laptop.width = 500
print('check lap1::::', laptop.dict())

t = Test()
t.laptop(laptop)
print('check lap2::::', t.get_laptop().dict())  # TODO set 할 때 instance로 했으면 get할 때는 dict로 보여줘야 함.

try:
    result = t.check()
    print('result::::', result)
except MyException as e:
    print('err message', e.get_message())  # err message width 는 50이상 200 사이로

