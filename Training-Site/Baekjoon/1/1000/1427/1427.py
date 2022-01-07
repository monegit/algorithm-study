n = input()
arr = []

for i in range(len(n)):
	arr.append(n[i])

arr.sort()

for i in range(len(n)):
	print(arr[len(n) - i - 1],end='')
print()
