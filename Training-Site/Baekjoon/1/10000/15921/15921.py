n = int(input())

a = [0] * 101
x = 0
y = 0

if n == 0:
	print("divide by zero")
else:
	case = list(map(int, input().split()))
	
	for i in range(n):
		a[case[i]] = a[case[i]] + 1
		x = x + case[i]
	
	for i in range(len(a)):
		if a[i] >= 1:
			y = y + (i * (a[i] / n))
	
	print(f'{round((x/n)/y,3):.2f}')
