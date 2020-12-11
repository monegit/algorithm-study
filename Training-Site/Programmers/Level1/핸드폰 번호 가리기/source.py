# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number:str)->str:
    answer = ''
    arr:list = []
    for _ in range(len(answer.join(phone_number[:-4]))):        
        arr.append("*")
    arr.append(phone_number[-4:])
    return ''.join(arr)

print(solution("01033334444"))