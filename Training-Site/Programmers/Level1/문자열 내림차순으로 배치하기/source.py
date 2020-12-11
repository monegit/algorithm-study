# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s: str):
    answer = []
    trunk1: list = []
    trunk2: list = []

    for i in range(len(s)):
        a = (lambda item: item)(ord(s[i]))
        if a > 90:
            trunk1.append(chr(a))

    for i in range(len(s)):
        a = (lambda item: item)(ord(s[i]))
        if a <= 90:
            trunk2.append(chr(a))

    trunk1.sort()
    trunk2.sort()
    answer = trunk1[::-1]+trunk2[::-1]
    return ''.join(answer)


print("gfedcbZ", solution("ZbcdAAQefg"))
