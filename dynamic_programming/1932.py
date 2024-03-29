from sys import stdin


N = int(stdin.readline())
P = [0] + [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : i번째 행의 j번째 열에 해당하는 지점까지 가는 경로에 있는 숫자의 최대 합
D = [[0 for _ in range(N)] for _ in range(N + 1)]

D[1][0] = P[1][0]

for i in range(2, N + 1):
	for j in range(i):
		if j == 0:
			D[i][j] = D[i - 1][j] + P[i][j]
		elif j == i - 1:
			D[i][j] = D[i - 1][j - 1] + P[i][j]
		else:
			D[i][j] = max(D[i - 1][j - 1], D[i - 1][j]) + P[i][j]

print(max(D[N]))
