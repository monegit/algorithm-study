n = int(input())

for i in range(n):
	for ii in range(i):
		print(' ',end='')
	for ii in range((n - i) * 2 - 1):
		print('*',end='')
	print()
