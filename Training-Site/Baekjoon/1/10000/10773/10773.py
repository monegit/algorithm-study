import sys

c = int(input())

arr = []
result = 0
for i in range(c):
    n = sys.stdin.readline().split()
    if n[0] == '0':
        arr.pop()
    else:
        arr.append(int(n[0]))

for i in arr:
    result += i

print(result)
