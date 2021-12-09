count = int(input())

result = []

for i in range(count):
	string = input()
	if result == []:
		result = [0] * len(string)
		for ii in range(len(string)):
			result[ii] = string[ii]
	else:
		for ii in range(len(string)):
			if result[ii] != string[ii]:
				result[ii] = "?"
			
print(''.join(str(_)for _ in result))
