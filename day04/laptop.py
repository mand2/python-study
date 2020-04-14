# 객체 instance 화 후 error raise
from day04.my_exception import MyException


class Laptop:
    def __init__(self):
        self.__keyboard = False
        self.__display = True
        self.__width = 0
        self.__height = 0

    @property
    def keyboard(self):
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self.__keyboard = keyboard

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, display):
        self.__display = display

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def check(self):
        print('type check start :::::')
        if isinstance(self.__width, int) and not isinstance(self.__width, bool):
            if 50 <= self.__width <= 200:
                result = True
            else:
                raise MyException('width 는 50이상 200 사이로')
        else:
            raise MyException('type err')

        return result

    def dict(self):
        laptop = {
            'keyboard': self.__keyboard,
            'display': self.__display,
            'width': self.__width,
            'height': self.__height
        }
        return laptop
