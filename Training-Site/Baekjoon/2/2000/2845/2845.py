# https://www.acmicpc.net/problem/2845

sizeArray = list(map(int, input().split()))
size = (lambda x, y: x*y)(sizeArray[0], sizeArray[1])
visitor = list(map(int, input().split()))

for i in range(len(visitor)):
    print(visitor[i]-size)