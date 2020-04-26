from sys import stdin


N, M = tuple(map(int, stdin.readline().split()))
A = [[0 for _ in range(M + 1)]] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : A[1][1] ~ A[i][j] 합
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	for j in range(1, M + 1):
		D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

K = int(stdin.readline())
for _ in range(K):
	i, j, x, y = tuple(map(int, stdin.readline().split()))
	print(D[x][y] - D[x][j - 1] - D[i - 1][y] + D[i - 1][j - 1])