info = []

for i in range(5):
	info.append(int(input()))
	
X = info[4] * info[0]
Y = info[1]

if info[2] < info[4]:
	Y = Y + ((info[4] - info[2]) * info[3])

print(min(X,Y))
