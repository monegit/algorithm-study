arr = []

for i in range(2):
	arr.append(sum(list(map(int, input().split()))))
	
print(max(arr))
