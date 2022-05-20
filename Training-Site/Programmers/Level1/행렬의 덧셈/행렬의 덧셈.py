def solution(arr1, arr2):
    answer = []

    for x in range(len(arr1)):
        arr = []
        for y in range(len(arr1[0])):
            arr.append(arr1[x][y]+arr2[x][y])
        answer.append(arr)

    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
# [[4,6],[7,9]]
