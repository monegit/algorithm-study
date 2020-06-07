count = int(input())
arr = []
for i in range(count):
    arr.append(input())

for i in range(len(arr)):
    a,b = map(int, arr[i].split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))