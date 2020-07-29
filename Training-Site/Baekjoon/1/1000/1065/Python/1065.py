_input = int(input())
count = 0

for i in range(1, _input + 1):
    if i < 100:
        count+=1
    else:
        arr = list(map(int, str(i)))
        if arr[0] - arr[1] == arr[1] - arr[2]:
            count+=1

print(count)