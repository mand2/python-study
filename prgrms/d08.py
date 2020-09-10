def solution(arr, commands):
    answer = []
    com_len = len(commands)
    for i in range(com_len):
        start = commands[i][0]-1
        end = commands[i][1]
        idx = commands[i][2]-1
        trimmed = arr[start:end]
        trimmed.sort()
        answer.append(trimmed[idx])
    return answer


def solution2(arr, commands):
    return list(map(lambda x: sorted(arr[x[0] - 1:x[1]])[x[2] - 1], commands))


arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

aw = solution(arr, commands)
print(aw)



