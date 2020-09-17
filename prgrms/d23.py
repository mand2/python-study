"""
멀쩡한 사각형
"""

from math import gcd


def getSafe(w, h):
    if w == h:
        return w * (w - 1)
    else:
        return w * h - (w + h - gcd(w, h))


def getSafe2(w, h):
    return w * h - (w + h - gcd(w, h))


"""
풀이 : 왜 w + h - gcd(w, h) 인가?
일단 w와 h의 최대공약수를 알아야 한다.
최대공약수로 w, h 를 나누면 구하기 쉬움.

즉 W H 를 gcd로 나눈 수를 w, h로 할 때 broken 된 정사각형의 개수는> 
    그래프를 그리면 쉽게 나온다. 글로 표현하니 어렵...
    w, h 좌표에서 "정사각형을 쪼개는 선(그래프의 기울기 = [h/w] )"가 
    의 선을 지나감 -> 마지막에 모이는 부분은 중복 구간이므로 w + h - 1.
    gcd 값을 곱해야 전체 그래프에서 쪼개진 정사각형을 구할 수 있음 > gcd * (w + h -1 ) => gcd * ( (W/gcd) + (H/gcd) - 1) => W + H - gcd 
"""


print(getSafe(3, 3))
print(getSafe(13, 4))
print(getSafe(30, 65))
print(getSafe(8, 12))

