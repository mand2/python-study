"""
수박수박수박수박수박수?
음 너무 쉬웠다...
"""


def watermelon(n):
    return ('수박'*int((n+1)/2))[:n]


print(watermelon(3))
print(watermelon(201))


