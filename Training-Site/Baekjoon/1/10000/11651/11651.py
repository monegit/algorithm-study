N = int(input())

arr = []

for _ in range(N):
    x, y = list(map(int, input().split()))

    arr.append((x, y))

arr.sort(key=lambda p: (p[1], p[0]))

for i in range(len(arr)):
    x, y = arr[i]

    print(x, y)
