# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr: list, divisor: int) -> list:
    answer = []
    arr.sort()

    for i in range(len(arr)):
        item = (lambda item,div:item[i]%div==0)(arr,divisor)
        if item == True:
            answer.append(arr[i])

    if answer == []:
        answer.append(-1)
    return answer


print("[5,10]", solution([5, 9, 7, 10], 5))
