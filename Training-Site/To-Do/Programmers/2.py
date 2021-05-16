def solution(priorities:list, location:int)->int:
    answer = 0

    for _ in range(len(priorities)):
        item = priorities.index(max(priorities))
        priorities[item]=0
        answer+=1

        if item==location:
            break
    return answer

# print(1, solution([2, 1, 3, 2,3],2))
print(5,solution([1, 1, 9, 1, 1, 1],0))