from sys import stdin


N = int(stdin.readline())
M = [None] + [tuple(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : M[i] ~ M[j]를 곱하는 최소 횟수
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	D[i][i] = 0

for d in range(1, N):
	for i in range(1, N - d + 1):
		s, e = i, i + d

		min_D = float('inf')
		for k in range(s, e):
			min_D = min(min_D, D[s][k] + D[k + 1][e] + M[s][0] * M[k][1] * M[e][1])
		D[s][e] = min_D

print(D[1][N])