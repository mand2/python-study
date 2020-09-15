"""
올바른 괄호
"""


def solution(s):
    point = 0
    s_len = len(s)
    if s[0] == ")" or s[s_len-1] == "(":
        return False
    else:
        for i in range(s_len):
            if point == 0 and s[i] == ")":
                return False
                break
            elif s[i] == ")":
                point -= 1
            else:
                point += 1
        return True if point == 0 else False


def solution2(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == "(" else x - 1
    return x == 0


test1 = "(()()"  # false
test2 = ")()("  # false
test3 = "(()())"  # true
test4 = "((()())"  # false
test5 = "(()("  # false
test6 = "(())()"  # true
test7 = "()))((()"  # false

print(solution(test1))
print(solution(test2))
print(solution(test3))
print(solution(test4))
print(solution(test5))

print(solution(test6))
print(solution2(test6))

print(solution(test7))
print(solution2(test7))

