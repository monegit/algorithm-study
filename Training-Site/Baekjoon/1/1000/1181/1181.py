import sys

count = int(input())

arr = []

for i in range(count):
    arr.append(sys.stdin.readline().split('\n')[0])

arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x: len(x))

for i in arr:
    print(i)
