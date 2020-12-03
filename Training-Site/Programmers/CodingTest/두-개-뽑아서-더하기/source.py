# https://programmers.co.kr/learn/courses/30/lessons/68644


def solution(numbers):
    answer = []

    # 인덱스 하나씩 구해옴
    for i in range(len(numbers)):
        for ii in range(len(numbers)):
            result = numbers[i]+numbers[ii]
            # 같은 인덱스의 값끼리는 더하지 않고, 같은 값이 포함되지 않을 때 answer에 추가
            if i != ii and result not in answer:
                answer.append(result)

    # 정렬
    answer.sort()
    return answer

# Test Case
print("Answer :", solution([5,0,2,7])) # Answer : [2,5,7,9,12]
print("Answer :", solution([2,1,3,4,1])) # Answer : [2,3,4,5,6,7]