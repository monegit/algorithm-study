# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 0

    arr = [s[i] for i in range(len(s))]
    arr.append(0)

    for a in range(len(arr)):
        if arr[a]!=0 and arr[a]==arr[a+1]:
            arr.pop(a)
            arr.pop(a+1)
            answer=1

    return answer


print(solution("abab"))
print(solution("baabaa"))
print(solution("aaab"))