arr = list(map(int, input().split()))

sum = 0
for i in range(len(arr)):
    sum+=arr[i]**2 ## Á¦°ö

print(sum%10)