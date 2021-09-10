from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [0] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j][0] : (i, j) 지점에서 출발할 때의 최대 가치 합 (아래로 가는 경우)
# D[i][j][1] : (i, j) 지점에서 출발할 때의 최대 가치 합 (왼쪽으로 가는 경우)
# D[i][j][2] : (i, j) 지점에서 출발할 때의 최대 가치 합 (오른쪽으로 가는 경우)
D = [[[0, 0, 0] for _ in range(M + 1)] for _ in range(N + 1)]

D[N][M][0] = A[N][M]
D[N][M][1] = A[N][M]
D[N][M][2] = A[N][M]
for j in reversed(range(1, M)):
	D[N][j][0] = float('-inf')
	D[N][j][1] = float('-inf')
	D[N][j][2] = A[N][j] + D[N][j + 1][2]

for i in reversed(range(1, N)):
	for j in range(1, M + 1):
		D[i][j][0] = A[i][j] + max(D[i + 1][j])

		if j == 1:
			D[i][j][1] = float('-inf')
		else:
			D[i][j][1] = A[i][j] + max(D[i][j - 1][0], D[i][j - 1][1])

	for j in reversed(range(1, M + 1)):
		if j == M:
			D[i][j][2] = float('-inf')
		else:
			D[i][j][2] = A[i][j] + max(D[i][j + 1][0], D[i][j + 1][2])

print(max(D[1][1][0], D[1][1][2]))
