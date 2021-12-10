N = input()
result = 0

for i in range(len(N)):
	if N[i] == '0':
		result = result + int(N[i-1]) * 10 - int(N[i-1])
	else:
		result = result + int(N[i])
		
print(result)
