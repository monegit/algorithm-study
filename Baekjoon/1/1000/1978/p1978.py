# First, make isPrime array / isPrime[n] is True when n is prime
isPrime = [True] * 1010

# 1 is not prime
isPrime[1] = False

# Multiples of some number is also not a prime
for i in range(2, int(1000 ** 0.5 )):
    for j in range(2*i, 1009, i):
        isPrime[j]=False


input()
arr = map(int,input().split())
cnt = 0
for a in arr:
    if isPrime[a]:
        cnt += 1
        
print(cnt)