from sys import stdin


N = int(stdin.readline())
A = [0] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : (i, j) 지점에서 출발하여 이동하는 경로의 개수
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in reversed(range(1, N + 1)):
	for j in reversed(range(1, N + 1)):
		if i == N and j == N:
			D[i][j] = 1
		elif A[i][j] != 0:
			if i + A[i][j] <= N:
				D[i][j] += D[i + A[i][j]][j]
			if j + A[i][j] <= N:
				D[i][j] += D[i][j + A[i][j]]

print(D[1][1])
