arr = [
	['black',0,1],
	['brown',1,10],
	['red',2,100],
	['orange',3,1000],
	['yellow',4,10000],
	['green',5,100000],
	['blue',6,1000000],
	['violet',7,10000000],
	['grey',8,100000000],
	['white',9,1000000000]
]

result = 0

for i in range(3):
	index = 0
	
	color = input()
	
	for ii in range(len(arr)):
		if arr[ii][0] == color:
			index = ii
			break
	
	if i == 0:
		result = result + arr[ii][1] * 10
	if i == 1:
		result = result + arr[ii][1]
	if i == 2:
		result = result * arr[ii][2]
		
print(result)
