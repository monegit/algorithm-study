price, count, money = map(int, input().split())

result = money - (price * count)

if result >= 0:
	print(0)
else:
	print(abs(result))
