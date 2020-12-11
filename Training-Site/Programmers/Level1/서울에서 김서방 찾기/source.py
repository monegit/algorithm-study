# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul:list):
    answer = ''

    answer = seoul.index("Kim")
    return "김서방은 {0}에 있다".format(answer)

print(solution(["dd","Kim"]))