x, y, z = map(int, input().split())
_max = 2147483647
a = int(x * y / z)
b = int(x / y * z)
	
print(max(a,b))
