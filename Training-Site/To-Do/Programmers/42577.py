# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

test1 = ["119", "97674223", "1195524421"]  # false
test2 = ["123", "456", "789"]  # true
test3 = ["12", "123", "1235", "567", "88"]  # false
test4 = ["123", "2344", "1231414", "14433"]


def solution(phone_book: list):
    first = phone_book[0]
    answer: bool = True

    for i in range(1, len(phone_book)):
        if(answer == True):
            if (first == phone_book[i][0:len(first)]):
                answer = False
            else:
                answer = True

    return answer


solution(test4)
