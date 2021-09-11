from sys import stdin


X = [0] + list(stdin.readline().rstrip())
Y = [0] + list(stdin.readline().rstrip())

X_len = len(X) - 1
Y_len = len(Y) - 1

# D[i][j] : X[i]와 Y[j]까지 고려했을 때 최장 공통 부분 수열의 길이
D = [[0 for _ in range(Y_len + 1)] for _ in range(X_len + 1)]

for i in range(1, X_len + 1):
	for j in range(1, Y_len + 1):
		if X[i] == Y[j]:
			D[i][j] = D[i - 1][j - 1] + 1
		else:
			D[i][j] = max(D[i - 1][j], D[i][j - 1])

print(D[X_len][Y_len])
