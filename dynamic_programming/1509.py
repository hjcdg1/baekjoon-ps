# Try again

from sys import stdin


S = [None] + list(stdin.readline().rstrip())
N = len(S) - 1

P = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	P[i][i] = True

for i in range(1, N):
	P[i][i + 1] = True if S[i] == S[i + 1] else False

for d in range(2, N):
	for i in range(1, N - d + 1):
		s, e = i, i + d
		if P[s + 1][e - 1] == True and S[s] == S[e]:
			P[s][e] = True
		else:
			P[s][e] = False

# D[i] : S[1] ~ S[i] 분할 개수의 최솟값
D = [-1 for _ in range(N + 1)]

D[1] = 1
D[2] = 1 if S[1] == S[2] else 2

for i in range(3, N + 1):
	if P[1][i]:
		D[i] = 1
	else:	
		min_D = D[i - 1] + 1
		for j in range(2, i):
			if P[j][i]:
				min_D = min(min_D, D[j - 1] + 1)
		D[i] = min_D

print(D[N])

"""
<첫 번째 풀이 : 시간 초과>
# D[i][j] : S[i:j + 1] 분할 개수의 최솟값
D = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]


for i in range(1, N + 1):
	D[i][i] = 1

for i in range(1, N):
	D[i][i + 1] = 1 if S[i] == S[i + 1] else 2

for d in range(2, N):
	for i in range(1, N - d + 1):
		s, e = i, i + d
		if D[s + 1][e - 1] == 1 and S[s] == S[e]:
			D[s][e] = 1
		else:
			D[s][e] = float('inf')
			for k in range(s, e):
				D[s][e] = min(D[s][e], D[s][k] + D[k + 1][e])

print(D[1][N])
"""