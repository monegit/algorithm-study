import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

nge = [-1 for _ in range(n)]
result = []

for i in range(n):
    while (len(result) != 0 and arr[result[-1]] < arr[i]):
        nge[result[-1]] = arr[i]
        result.pop()
    result.append(i)

print(*nge)
