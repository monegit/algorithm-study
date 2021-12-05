dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(int(input())):
	n = int(input())
	for i in range(10, n):
		dp.append(dp[i-1]+1)
		
		dp[i] = dp[i-2:i-1][0] + dp[i-3:i-2][0]
	
	print(dp[n-1])
