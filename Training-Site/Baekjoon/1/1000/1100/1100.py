arr = []
count = 0

for i in range(8):
    arr.append(input())

# white first
for i in range(len(arr)):
    if i % 2 == 0:
        for ii in range(len(arr[i])):
            if ii % 2 == 0 and arr[i][ii] == "F":
                count = count + 1

# black first
for i in range(len(arr)):
    if i % 2 == 1:
        for ii in range(len(arr[i])):
            if ii % 2 == 1 and arr[i][ii] == "F":
                count = count + 1

print(count)
