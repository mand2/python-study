"""
list, tuple
"""
# 모자를 앞 / 뒤로 쓴 사람 list #17
caps1 = ['F', 'F', 'B', 'F', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'B', 'B', 'F', 'F', 'B', 'F']
caps2 = ['F', 'F', 'B', 'F', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'B', 'B', 'F', 'F', 'B', 'B']


# 연속으로 같은 모자를 쓴 사람끼리 그룹 만들기
def make_group(caps):
    start = 0
    size = len(caps)
    groups = []
    for i in range(1, size):
        if caps[start] != caps[i]:
            groups.append((start, i - 1))
            start = i
    groups.append((start, size-1))

    index = len(groups)
    index_call(1, index, groups)


# 효율적으로 모자 뒤집으라 말하기
def index_call(start, index, groups):
    for i in range(start, index, 2):
        if groups[i][0] == groups[i][1]:
            print('guest #', groups[i][0], 'flip your cap !')
        else:
            print('guests from #', groups[i][0], 'through #', groups[i][1], 'flip your caps !')


make_group(caps1)
# make_group(caps2)
