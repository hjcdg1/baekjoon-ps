from sys import stdin


N = int(stdin.readline())
P = [None] + [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i] : i번째 층까지 가는 경로에 있는 숫자의 최대 합
D = [None] + [[-1] * N for _ in range(N)]

D[1][0] = P[1][0]

for i in range(2, N + 1):
	for j in range(i):
		if j == 0:
			D[i][j] = D[i - 1][j] + P[i][j]
		elif j == i - 1:
			D[i][j] = D[i - 1][j - 1] + P[i][j]
		else:
			D[i][j] = max(D[i - 1][j - 1], D[i - 1][j]) + P[i][j]

print(max(D[i]))