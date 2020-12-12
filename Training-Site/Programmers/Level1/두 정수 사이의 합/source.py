def solution(a: int, b: int) -> int:
    # 낮은 값과 높은 값을 오름차순으로 정렬해줌
    minmax = [a, b]
    minmax.sort()

    # 사이 값들을 arr에 추가해줌
    arr = [i for i in range(minmax[0], minmax[1]+1)]

    return sum(arr)


print(solution(3, 5))
