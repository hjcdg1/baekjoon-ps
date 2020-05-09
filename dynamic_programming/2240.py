from sys import stdin


T, W = tuple(map(int, stdin.readline().split()))
A = [-1] + [int(stdin.readline()) for _ in range(T)]

# D[i][j][k] : 떨어질 자두가 i개 남았을 때, 남은 이동 횟수가 j이고 현재 위치가 k인 경우
D = [[[0, 0] for _ in range(W + 1)] for _ in range(T + 1)]

for i in range(1, T + 1):
	for j in range(W + 1):
		if j == 0:
			if A[-i] == 1:
				D[i][j][0] = 1 + D[i - 1][j][0]
				D[i][j][1] = D[i - 1][j][1]
			else:
				D[i][j][0] = D[i - 1][j][0]
				D[i][j][1] = 1 + D[i - 1][j][1]
		else:
			if A[-i] == 1:
				D[i][j][0] = max(1 + D[i - 1][j][0], D[i - 1][j - 1][1])
				D[i][j][1] = max(D[i - 1][j][1], 1 + D[i - 1][j - 1][0])
			else:
				D[i][j][0] = max(D[i - 1][j][0], 1 + D[i - 1][j - 1][1])
				D[i][j][1] = max(1 + D[i - 1][j][1], D[i - 1][j - 1][0])

print(D[T][W][0])