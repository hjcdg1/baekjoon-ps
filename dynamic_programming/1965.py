# Try again

from sys import stdin


N = int(stdin.readline())
S = [-1] + list(map(int, stdin.readline().split()))

# D[i] : S[i]가 마지막인 LIS의 길이
D = [0 for _ in range(N + 1)]

D[1] = 1

for i in range(2, N + 1):
	max_D = 1
	for j in range(1, i):
		if S[j] < S[i] and D[j] + 1 > max_D:
			max_D = D[j] + 1
	D[i] = max_D

print(max(D[1:]))