from sys import stdin


N = int(stdin.readline())
A = [[0 for _ in range(N + 1)]] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : (i, j)에서 출발하는 경우의 답
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in reversed(range(1, N + 1)):
	for j in reversed(range(1, N + 1)):
		if i == N and j == N:
			D[i][j] = 1
		else:
			if i + A[i][j] <= N:
				D[i][j] += D[i + A[i][j]][j]
			if j + A[i][j] <= N:
				D[i][j] += D[i][j + A[i][j]]

print(D[1][1])