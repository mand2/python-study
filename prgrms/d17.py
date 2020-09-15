"""모의고사"""

s1 = [1, 2, 3, 4, 5]
s2 = [2, 1, 2, 3, 2, 4, 2, 5]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            score[0] += 1
        if answers[i] == s2[i % 8]:
            score[1] += 1
        if answers[i] == s3[i % 10]:
            score[2] += 1
    print('answer', score[0], score[1], score[2])
    print('max?', max(score))

    p = list(map(lambda x: (score.index(x) if x == max(score) else None), score))
    print('t', list(filter(lambda x: x == max(score), score)))
    print('p', p)
    # idx 를 가져오려면 enumerate() 사용해야 함.
    return [ idx + 1 for idx, i in enumerate(score) if i == max(score)]


print(solution([1, 2, 3, 4, 5]))

print(solution([1, 3, 2, 4, 2]))

print(solution([1, 3]))

