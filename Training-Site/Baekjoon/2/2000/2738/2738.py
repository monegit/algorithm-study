import sys

n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for e in range(m):
        sys.stdout.write(str(a[i][e] + b[i][e])+' ')
    sys.stdout.write('\n')
