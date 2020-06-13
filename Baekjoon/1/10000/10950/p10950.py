count = int(input())
arr = []
for i in range(count):
    arr.append(input())

for i in range(len(arr)):
    a,b = map(int, arr[i].split())
    print(a+b)