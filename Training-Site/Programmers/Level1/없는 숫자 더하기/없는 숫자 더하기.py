def solution(numbers):
    num = [i for i in range(10)]

    for i in numbers:
        num.remove(i)

    return sum(num)


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
