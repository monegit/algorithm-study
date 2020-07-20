# problem 2588

a = int(input())
b = int(input())
arr = list(map(int, str(b)))

for i in reversed(range(3)): # reversed를 이용해 2부터 0까지 감소
    print(a * arr[i])
print(a*b)