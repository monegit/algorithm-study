y, x = map(int, input().split())

arr = [['.' for i in range(x)] for i in range(y)]


for i in range(len(arr)):
	s = input()
	
	for ii in range(len(arr[i])):
		if s[ii] != '.':
			arr[i][ii] = s[ii]
			arr[i][-(ii + 1)] = s[ii]
			
for i in range(len(arr)):
	for ii in range(len(arr[i])):
		print(arr[i][ii], end='')
	print()
