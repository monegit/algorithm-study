import sys

n = [0]*10000

for _ in range(int(input())):
	i = int(sys.stdin.readline())-1
	n[i] = n[i] + 1
	
for i in range(len(n)):
	if n[i] != 0:
		for ii in range(n[i]):
			print(i+1)
