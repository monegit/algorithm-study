import sys

N, M = map(int, sys.stdin.readline().split())

arr = [i+1 for i in range(N)]

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())

    if (i > N or j > N):
        continue

    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

for i in arr:
    sys.stdout.write(str(i)+' ')
