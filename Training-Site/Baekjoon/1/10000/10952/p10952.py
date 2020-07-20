arr = []

while True:
    arr.append(input())
    if arr[len(arr)-1] == "0 0":
        break

for i in range(len(arr)-1):
    a,b = map(int, arr[i].split())
    print(a+b)