from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [None] + [[None] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : A[1][1] ~ A[i][j] 합
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	for j in range(1, M + 1):
		D[i][j] = A[i][j] + D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1]

K = int(stdin.readline())
for _ in range(K):
	i, j, x, y = list(map(int, stdin.readline().split()))
	print(D[x][y] - D[i - 1][y] - D[x][j - 1] + D[i - 1][j - 1])
