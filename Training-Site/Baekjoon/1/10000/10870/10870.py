dp = [0,0,1,1]

n = int(input())

for i in range(4,n+2):
	dp.append(dp[i-1]+1)
	dp[i] = dp[i-2]+dp[i-1]


if n == 0: print(0)
else: print(dp[-1])
