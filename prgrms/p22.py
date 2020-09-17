"""1차 비밀지도"""


def secret_map(n, arr1, arr2):
    test = []
    for i in range(n):
        s = format(arr1[i] | arr2[i], 'b')
        for j in range(n - len(s)):
            s = '0' + s
        s = s.replace('1', '#').replace('0', ' ')
        test.append(s)  # [63, 57, 51, 30, 31, 58]
    print(test)


secret_map(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#').replace('0', ' ')
        answer.append(a12)
    return answer
