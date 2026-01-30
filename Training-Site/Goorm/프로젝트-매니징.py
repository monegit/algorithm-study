# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
T, M = map(int, input().split())

for i in range(N):
	M += int(input())

hours = int(M / 60)

print((T + hours) % 24, M % 60)