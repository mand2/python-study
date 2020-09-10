"""
문자열 내 마음대로 정렬하기
strings , n + 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
"""


def solution(strings, n):
    # tuple 로 구성된 list 로 반환
    my = list(map(lambda x: (x[n], strings.index(x), x), strings))
    print('my_sort_bef', my)

    # abc 순으로 sort
    my.sort(key=lambda x: (x[0], strings[x[1]]))
    print('my_sort_aft', my)

    # 원래 값만 리스트로 보여줌
    print('answer', list(map(lambda x: x[2], my)))
    return list(map(lambda x: x[2], my))


def solution2(strings, n):
    # 중복으로 있는 alphabet idx
    print('sort?', sorted(strings, key=lambda x: (x[n], x)))
    return sorted(strings, key=lambda x: (x[n], x))


test_str = ['sun', 'cat', 'bed', 'car']  # ['car', 'cat', 'bed', 'sun']
test_str2 = ['abce', 'abcd', 'cdx']  # ['abcd', 'abce', 'cdx']

solution(test_str, 1)
solution(test_str2, 2)
print('------------------------------------')
solution2(test_str, 1)
solution2(test_str2, 2)
