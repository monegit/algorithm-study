N = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = list(map(int, input().split()))

    for i in range(y, y+10):
        arr[i][x:x+10] = [1 for _ in range(10)]

count = sum(row.count(1) for row in arr)
print(count)
