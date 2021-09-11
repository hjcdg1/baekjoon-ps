from sys import stdin


X = [0] + list(stdin.readline().rstrip())
Y = [0] + list(stdin.readline().rstrip())
Z = [0] + list(stdin.readline().rstrip())

X_len = len(X) - 1
Y_len = len(Y) - 1
Z_len = len(Z) - 1

# D[i][j][k] : X[i], Y[j], Z[k]까지 고려했을 때 최장 공통 부분 수열의 길이
D = [[[0 for _ in range(Z_len + 1)] for _ in range(Y_len + 1)] for _ in range(X_len + 1)]

for i in range(1, X_len + 1):
	for j in range(1, Y_len + 1):
		for k in range(1, Z_len + 1):
			if X[i] == Y[j] == Z[k]:
				D[i][j][k] = D[i - 1][j - 1][k - 1] + 1
			else:
				D[i][j][k] = max(D[i - 1][j][k], D[i][j - 1][k], D[i][j][k - 1])

print(D[X_len][Y_len][Z_len])
