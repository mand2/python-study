# 커스텀 exception
class MyException(Exception):
    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message
