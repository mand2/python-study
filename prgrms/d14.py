"""
월간코드챌린지 시즌1: 삼각 달팽이
"""


def solution(n):
    answer = [[0 for x in range(y)] for y in range(1, n + 1)]
    print('result', answer)

    num = 1
    x = -1
    y = 0
    test = n % 3
    print('n', n, 'n % 3 = test::', test)
    for i in range(n, 0, -1):
        for j in range(i):
            print('n', n, 'num', num, '\ti', i, 'j', j)
            if n % 3 == test:
                print('n % 3 == test', n, test)
                x = x + 1
            elif n % 3 == (test - 1) or n % 3 == (test + 2):
                print('n % 3 == (test - 1)', n, test, (test-1))
                y += 1
            else:
                print('else')
                x -= 1
                y -= 1
            print('x y', x, y)
            answer[x][y] = num
            print('x y', x, y, ':: result', answer[x][y])
            num = num + 1

        n = n - 1

    import itertools
    print(list(itertools.chain(*answer)))


solution(7)
solution(2)
solution(3)
solution(6)
