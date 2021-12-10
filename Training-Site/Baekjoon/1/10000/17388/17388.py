S, K, H = map(int, input().split())
univ = {S:"Soongsil", K:"Korea", H:"Hanyang"}

call = min(S, K, H)

if S + K + H >= 100:
	print("OK")
else:
	print(univ[min(S,K,H)])
