import sys

count = int(input())

arr = []

for i in range(count):
    r = sys.stdin.readline().split()

    if r[0] == "push":
        arr.append(int(r[1]))
    if r[0] == "pop":
        if arr == []:
            print(-1)
        else:
            print(arr[0])
            arr.pop(0)
    if r[0] == "size":
        print(len(arr))
    if r[0] == "empty":
        if arr == []:
            print(1)
        else:
            print(0)
    if r[0] == "front":
        if arr == []:
            print(-1)
        else:
            print(arr[0])
    if r[0] == "back":
        if arr == []:
            print(-1)
        else:
            print(arr[-1])
