n = int(input())

for i in range(n):
	for _ in range(n - i - 1):
		print(' ', end='')
	print('*',end='')
	for ii in range(i * 2):
		print('*',end='')
	print()
