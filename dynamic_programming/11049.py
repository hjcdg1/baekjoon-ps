from sys import stdin


N = int(stdin.readline())
M = [0] + [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : M[i] ~ M[j]를 곱하는 최소 횟수
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for d in range(1, N):
	for i in range(1, N - d + 1):
		start = i
		end = i + d

		min_D = float('inf')
		for k in range(start, end):
			min_D = min(min_D, D[start][k] + D[k + 1][end] + M[start][0] * M[k][1] * M[end][1])
		D[start][end] = min_D

print(D[1][N])
