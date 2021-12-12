arr = []

for i in range(6):
	arr.append(int(input()))

print((arr[0]+arr[1]+arr[2]+arr[3])-min(arr[0],arr[1],arr[2],arr[3])+(arr[4]+arr[5])-min(arr[4],arr[5]))
