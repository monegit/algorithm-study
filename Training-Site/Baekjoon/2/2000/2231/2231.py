n = input()
true = 0
false = 0

def s(a):
	r = 0
	
	for i in range(len(a)):
		r = int(a[i]) + r
		
	r = r + int(a)
		
	return r

for i in range(int(n)+1):
	if int(n) == s(str(i)):
		print(i)
		break
	if int(n) <= i:
		print(0)
		break
