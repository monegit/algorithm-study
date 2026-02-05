N = int(input())
arr = list(map(int, input().split()))
ready_line = [0]

while len(arr) > 0:
    if arr[0] == N-(len(arr)+len(ready_line))+2:
        arr.pop(0)
    elif ready_line[-1] == N-(len(arr)+len(ready_line))+2:
        ready_line.pop()
    else:
        ready_line.append(arr[0])
        arr.pop(0)

for i in range(len(ready_line)):
    if ready_line[-1] == N-(len(arr)+len(ready_line))+2:
        ready_line.pop()
    else:
        break

if arr == [] and ready_line == [0]:
    print('Nice')
else:
    print('Sad')
