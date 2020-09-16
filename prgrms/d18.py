"""가운데 글자 가져오기"""


def solution(s):
    s_len = len(s)

    if s_len % 2 == 0:
        return s[s_len // 2 - 1] + s[s_len // 2]
    else:
        return s[s_len // 2]


def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]


