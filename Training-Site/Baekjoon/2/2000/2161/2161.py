from collections import deque

n = int(input())
card = deque()
throwList = []
count = 0

for i in range(n):
	card.append(i+1)

while True:
	if len(card) == 1:
		break
	if count == 0:
		throwList.append(card.popleft())
	elif count % 2 == 1:
		card.append(card.popleft())
	elif count % 2 == 0:
		throwList.append(card.popleft())
	count = count + 1

for i in range(len(throwList)):
	print(throwList[i],end=' ')
print(card[0])
