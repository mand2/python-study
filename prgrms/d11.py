""""
2019 카카오개발자 겨울인턴십 : 크레인 인형뽑기 게임
"""


def solution(board, moves):
    b_len = len(board)
    sack = [-1]
    answer = 0

    for i in moves:
        for j in range(b_len):
            doll = board[j][i-1]
            if doll > 0:
                if sack[-1] == doll:
                    sack.pop()
                    board[j][i-1] = 0
                    answer += 2
                else:
                    sack.append(doll)
                    board[j][i-1] = 0
                break
    print(answer)
    return answer


"""
real_idx = moves[i]-1
다음은 같은 결과를 나타낸다.
list(map(lambda x: x[real_idx], board))
[x[real_idx] for x in board]
"""


test_b = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 3],
          [0, 2, 5, 0, 1],
          [4, 2, 4, 4, 2],
          [3, 5, 1, 3, 1]]
test_m = [1, 5, 3, 5, 1, 2, 1, 4]
solution(test_b, test_m)

