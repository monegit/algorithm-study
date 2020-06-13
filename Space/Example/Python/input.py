# Nomal Int Type Input
_input = int(input())

for i in range(_input):
    print(i)

# List Type Input
_input = list(input().split())

for i in range(len(_input)):
    print(i)

# Practice Input
# _input array each value plus 1
_input = list(map(int, input().split()))

for i in range(len(_input)):
    print(i+1)