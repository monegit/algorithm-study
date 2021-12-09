day = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(day):
	a = a - c
	b = b - d
	if a <= 0 and b <= 0:
		break
	day = day - 1
		
print(day - 1)
