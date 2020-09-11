"""
2016년
2016.01.01 금
a월 b일 무슨 요일?
"""


month = [31, 29, 31, 30, 31, 30,
         31, 31, 30, 31, 30, 31]
dates = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']


def solution1(a, b):
    days = 0
    for i in range(a-1):
        days += month[i]
    days = (days + b) % 7
    # 기준일 dates[5]
    print(dates[5+days-1-7])
    return dates[5+days-1-7]




"""
날짜를 구할 때 -1 을 하는 이유 : 
1월 1일이 금요일(5) 이라서, 한 주를 채우려면 아직 하루가 남음. 
"""


def solution2(a, b):
    days = sum(month[:a-1]) + b
    print(dates[5 + (days % 7) - 1 - 7])
    return dates[5 + (days % 7) - 1 - 7]


def solution3(a, b):
    days = (sum(month[:a - 1]) + b - 1) % 7
    print(dates[5 + days - 7])
    return dates[5 + days - 7]


solution1(5, 24)
solution2(5, 24)
solution3(5, 24)
