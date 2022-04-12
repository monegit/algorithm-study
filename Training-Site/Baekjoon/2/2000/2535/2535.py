count = int(input())

arr = []
win = []
win_national = [0]*1001

for i in range(count):
    national, student, score = input().split()
    arr.append([int(score), f"{national} {student}"])

arr.sort(key=lambda x: x[0], reverse=True)

for i in range(count):
    if len(win) < 3 and win_national[int(arr[i][1][0])] < 2:
        win_national[int(arr[i][1][0])] += 1
        win.append(arr[i][1])

for i in win:
    print(i)
