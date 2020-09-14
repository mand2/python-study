"""
월간코드챌린지 시즌1: 두 개 뽑아서 더하기
"""


def solution(numbers):
    n_len = len(numbers)
    answer = []
    for i in range(n_len - 1):
        for j in range(i+1, n_len):
            if i != j:
                print('i', i, 'j', j, 'i+j', (numbers[i] + numbers[j]))
                answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))


n_list1 = [2, 1, 3, 4, 1]
n_list2 = [5, 0, 2, 7]

print('answer', solution(n_list1))
print('-----------')
print('answer', solution(n_list2))
