x,y,z = map(int, input().split())
arr = [0] * 7
won = 0

arr[x] = arr[x] + 1
arr[y] = arr[y] + 1
arr[z] = arr[z] + 1

for i in range(len(arr)):
	if arr[i] == 2:
		won = 1000 + i * 100
		break
	elif arr[i] == 3:
		won = 10000 + i * 1000
		break
	else:
		won = max([x,y,z]) * 100
		
print(won)
