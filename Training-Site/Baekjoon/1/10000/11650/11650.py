import sys

n = list()

for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    n.append([x, y])

n.sort()

for i in n:
    print(i[0], i[1])
