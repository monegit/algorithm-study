import sys

for _ in range(3):
	count = int(input())
	result = 0
	
	for ii in range(count):
		result = result + int(sys.stdin.readline())
	
	if result < 0:
		print('-')
	elif result > 0:
		print('+')
	elif result == 0:
		print('0')
