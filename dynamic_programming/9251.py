from sys import stdin


X = list(stdin.readline().rstrip())
Y = list(stdin.readline().rstrip())
N, M = len(X), len(Y)

# D[i][j] : X[i], Y[j]까지만 고려했을 때 최장 공통 부분 수열의 길이
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	for j in range(1, M + 1):
		if X[i - 1] != Y[j - 1]:
			D[i][j] = max(D[i - 1][j], D[i][j - 1])
		else:
			D[i][j] = D[i - 1][j - 1] + 1

print(D[N][M])