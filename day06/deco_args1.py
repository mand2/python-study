"""
accepting arguments in Decorator functions
ref: https://www.datacamp.com/community/tutorials/decorators-python

learn how to manage arguments - called `*args`
"""


def decorator_with_args(function):
    def wrapper_accepting_args(arg1, arg2):
        print('my arguments are: {0}, {1}'.format(arg1, arg2))

        # 인자 변환해보기
        arg1 = '✨' + arg1.upper() + '✨'
        arg2 = arg2.lower() + '~~~'
        print('my converted arguments are: {0}, {1}'.format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_args


@decorator_with_args
def cities(first, second):
    print('I\'d love to visit {0} first and then {1}.'.format(first, second))


cities('Busan', 'Jeju')

# ###### result ######
# my arguments are: Busan, Jeju
# my converted arguments are: ✨BUSAN✨, jeju~~~
# I'd love to visit ✨BUSAN✨ first and then jeju~~~.


"""
결론:
    cities()에 어떤 args가 들어가든 간에
    - 첫번째 인자는 대문자로 변경되며 이모티콘 '✨'이 앞뒤로 들어간다. 
    - 두번째 인자는 소문자로 변경되며 '~~~' 이 뒤에 들어간다.
"""

