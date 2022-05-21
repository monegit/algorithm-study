arr = []

for _ in range(3):
    arr.append(int(input()))

if not sum(arr) == 180:
    print("Error")
elif set(arr) == {60}:
    print("Equilateral")
elif sum(arr) == 180 and len(set(arr)) >= 3:
    print("Scalene")
elif sum(arr) == 180 and len(set(arr)) >= 2:
    print("Isosceles")
