count = int(input())

for i in range(count):
	coupon = float(input())
	print(f"${(coupon*(1-20/100)):.2f}")
