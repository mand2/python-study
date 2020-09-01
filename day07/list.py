"""
list : java 의 array 와 비슷.
다른 형태의 값을 넣어도 된다. ex) a = ['abc', 2, 0.44]
탐색 시 전 / 후 탐색 가능. ex) list[-2] = 리스트 끝에서부터 2번째
"""

"""
정렬된 리스트 ll + 정수 x
x의 값을 ll에 삽입
"""


def insertNum(ll, x):
    list_size = len(ll)
    if ll[-1] < x:
        ll.append(x)

    for i in range(list_size):
        if x < ll[i]:
            ll.insert(i, x)
            break
    return ll


my_list = [2, 5, 7, 11, 48, 99]
my_x = 9
answer = insertNum(my_list, my_x)
print(answer)

"""
list 에 x가 있으면 x의 인덱스 모두 반환, 없으면 -1
"""


def checkIndex(ll, x):
    a_list = []
    n = len(ll)

    print('inserted list', ll)
    if x in ll:
        for i in range(n):
            if ll[i] == x:
                a_list.append(i)
    else:
        a_list.append(-1)
    return a_list


def checkIndex2(ll, x):
    if x in ll:
        return [idx for idx, val in enumerate(ll) if x == val]
    else:
        return [-1]


