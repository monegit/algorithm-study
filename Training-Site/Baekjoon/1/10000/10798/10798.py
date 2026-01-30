arr = []

result = ""

for _ in range(5):
    arr.append(list(input()))

for x in range(15):
    for y in range(len(arr)):
        try:
            result += arr[y][x]
        except:
            continue


print(result)
