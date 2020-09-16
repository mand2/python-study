"""시저암호"""

s = 'abcdefghijklmnopqrstuvwzyx'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = ' '
s = sorted(s, reverse=True)
b = sorted(b, reverse=True)


def ceasar_pass(p, n):
    answer = ''
    for i in p:
        if i in s:
            answer += s[s.index(i) - n]
        if i in b:
            answer += b[b.index(i) - n]
        if i == m:
            answer += m
    print('answer', answer)


ceasar_pass("a B z", 4)


def caesar(p, n):
    p = list(p)
    for i in range(len(p)):
        if p[i].isupper():
            p[i] = chr((ord(p[i])-ord('A') + n) % 26 + ord('A'))
        elif p[i].islower():
            p[i] = chr((ord(p[i])-ord('a') + n) % 26 + ord('a'))

    return "".join(p)


def caesar2(p, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in p:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)
