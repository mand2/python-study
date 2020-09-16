"""
문자열 내림차순으로 배치하기
"""


def order_desc(s):
    print("".join(sorted(s, reverse=True)))


order_desc("Zbcdefg")

