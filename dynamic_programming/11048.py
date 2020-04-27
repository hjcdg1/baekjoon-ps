from sys import stdin


N, M = tuple(map(int, stdin.readline().split()))
A = [[0 for _ in range(M + 1)]] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : A[i][j]까지 갈 때 획득할 수 있는 최대 사탕 개수
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	for j in range(1, M + 1):
		D[i][j] = max(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + A[i][j]

print(D[N][M])