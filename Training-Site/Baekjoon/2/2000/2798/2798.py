n, m = map(int, input().split())


def solution(m: int, arr: list):
    max = 0
    for i1, n1 in enumerate(arr):
        for i2, n2 in enumerate(arr):
            if (i1 == i2):
                continue
            else:
                for i3, n3 in enumerate(arr):
                    if (i1 == i3 or i2 == i3):
                        continue
                    else:
                        sum = n1+n2+n3
                        if (sum > max and sum <= m):
                            max = sum
                        else:
                            continue
    print(max)


solution(m, list(map(int, input().split())))
