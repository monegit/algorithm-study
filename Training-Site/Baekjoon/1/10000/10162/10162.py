time = int(input())

a = 0
b = 0
c = 0

elec = [60*5, 60, 10]

for i in range(len(elec)):
	if i == 0:
		a = time // elec[i]
		time = time - (a * elec[i])
	if i == 1:
		b = time // elec[i]
		time = time - (b * elec[i])
	if i == 2:
		c = time // elec[i]
		time = time - (c * elec[i])

if time == 0:
	print(a,b,c)
else:
	print(-1)
