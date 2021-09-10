from sys import stdin


T, W = list(map(int, stdin.readline().split()))
P = [0] + [int(stdin.readline()) for _ in range(T)]

# D[i][j][p] : i초가 되기 직전, 남은 이동 가능 횟수가 j번이고 위치가 p일 때
D = [[[0, 0, 0] for _ in range(W + 1)] for _ in range(T + 1)]

for j in range(W + 1):
	D[T][j][1] = 1 if P[T] == 1 or j >= 1 else 0
	D[T][j][2] = 1 if P[T] == 2 or j >= 1 else 0

for i in reversed(range(1, T)):
	for j in range(W + 1):
		# 1번 나무에서 자두가 떨어지는 경우
		if P[i] == 1:
			# 현재 위치가 1번 나무인 경우
			D[i][j][1] = 1 + D[i + 1][j][1]
			if j >= 1:
				D[i][j][1] = max(D[i][j][1], D[i + 1][j - 1][2])

			# 현재 위치가 2번 나무인 경우
			D[i][j][2] = D[i + 1][j][2]
			if j >= 1:
				D[i][j][2] = max(D[i][j][2], 1 + D[i + 1][j - 1][1])

		# 2번 나무에서 자두가 떨어지는 경우
		else:
			# 현재 위치가 1번 나무인 경우
			D[i][j][1] = D[i + 1][j][1]
			if j >= 1:
				D[i][j][1] = max(D[i][j][1], 1 + D[i + 1][j - 1][2])

			# 현재 위치가 2번 나무인 경우
			D[i][j][2] = 1 + D[i + 1][j][2]
			if j >= 1:
				D[i][j][2] = max(D[i][j][2], D[i + 1][j - 1][1])

print(D[1][W][1])
