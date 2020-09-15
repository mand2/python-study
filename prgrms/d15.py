"""
최솟값 만들기
"""


def solution(A, B):
    A.sort()
    B.sort()
    B.reverse()
    print(A)
    print(B)
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    print(answer)


def solution2(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))


def solution3(A, B):
    return sum(map(lambda a, b: a * b, sorted(A), sorted(B, reverse=True)))


a_1 = [1, 2]
b_1 = [3, 4]
a_2 = [1, 4, 2]
b_2 = [5, 4, 4]

solution(a_2, b_2)
solution(a_1, b_1)
