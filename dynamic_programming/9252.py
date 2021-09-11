from sys import stdin


X = [0] + list(stdin.readline().rstrip())
Y = [0] + list(stdin.readline().rstrip())

X_len = len(X) - 1
Y_len = len(Y) - 1

# D[i][j] : X[i]와 Y[j]까지 고려했을 때 최장 공통 부분 수열의 길이
D = [[0 for _ in range(Y_len + 1)] for _ in range(X_len + 1)]

# M[i][j] : D[i][j]의 출처(방향) (1: 위, 2: 왼쪽, 3: 대각선)
M = [[0 for _ in range(Y_len + 1)] for _ in range(X_len + 1)]

for i in range(1, X_len + 1):
	for j in range(1, Y_len + 1):
		if X[i] == Y[j]:
			D[i][j] = D[i - 1][j - 1] + 1
			M[i][j] = 3
		else:
			if D[i - 1][j] >= D[i][j - 1]:
				D[i][j] = D[i - 1][j]
				M[i][j] = 1
			else:
				D[i][j] = D[i][j - 1]
				M[i][j] = 2

print(D[X_len][Y_len])
if D[X_len][Y_len] > 0:
	result = []
	i = X_len
	j = Y_len
	while i > 0 and j > 0:
		if M[i][j] == 1:  # 위
			i -= 1
		elif M[i][j] == 2:  # 왼쪽
			j -= 1
		else:  # 대각선
			result.append(X[i])
			i -= 1
			j -= 1
	print(''.join(reversed(result)))
