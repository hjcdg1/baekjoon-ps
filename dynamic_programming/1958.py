from sys import stdin


X = [None] + list(stdin.readline().rstrip())
Y = [None] + list(stdin.readline().rstrip())
Z = [None] + list(stdin.readline().rstrip())

X_len = len(X) - 1
Y_len = len(Y) - 1
Z_len = len(Z) - 1

# D[i][j][w] : X[i], Y[j], Z[w]가 끝인 LCS의 길이
D = [[[0 for _ in range(Z_len + 1)] for _ in range(Y_len + 1)] for _ in range(X_len + 1)]

for i in range(1, X_len + 1):
	for j in range(1, Y_len + 1):
		for w in range(1, Z_len + 1):
			if X[i] != Y[j] and Y[j] != Z[w] and Z[w] != X[i]:
				D[i][j][w] = max(D[i][j][w - 1], D[i][j - 1][w], D[i - 1][j][w])
			elif X[i] == Y[j] and Y[j] == Z[w]:
				D[i][j][w] = D[i - 1][j - 1][w - 1] + 1
			else:
				if X[i] == Y[j]:
					D[i][j][w] = max(D[i - 1][j - 1][w], D[i][j][w - 1])
				elif Y[j] == Z[w]:
					D[i][j][w] = max(D[i][j - 1][w - 1], D[i - 1][j][w])
				else:
					D[i][j][w] = max(D[i - 1][j][w - 1], D[i][j - 1][w])

max_D = float('-inf')
for i in range(1, X_len + 1):
	for j in range(1, Y_len + 1):
		for w in range(1, Z_len + 1):
			max_D = max(max_D, D[i][j][w])
print(max_D)