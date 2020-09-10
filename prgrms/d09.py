"""같은 숫자는 싫어 LEVEL 1
배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지
"""


def solution(arr):
    arr_len = len(arr)
    idx = 0
    answer = [arr[idx]]

    for i in range(1, arr_len):
        start = arr[idx]
        if start != arr[i]:
            answer.append(arr[i])
            idx = i
    return answer


def solution2(arr):
    answer = []

    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer


my_arr = [1, 1, 3, 3, 0, 1, 1]
my_arr2 = [4, 4, 4, 3, 3, 0]

print(solution(my_arr))
print(solution2(my_arr2))


