from sys import stdin


A = [-1] + list(stdin.readline().rstrip())
B = [-1] + list(stdin.readline().rstrip())

A_len = len(A) - 1
B_len = len(B) - 1

# D[i][j] : A[i], B[j]까지만 봤을 때의 LCS의 길이
D = [[0 for _ in range(B_len + 1)] for _ in range(A_len + 1)]

# M[i][j] : D[i][j]의 출처(방향) (1: 위, 2: 왼쪽, 3: 대각선)
M = [[0 for _ in range(B_len + 1)] for _ in range(A_len + 1)]

for i in range(1, A_len + 1):
	for j in range(1, B_len + 1):
		if A[i] == B[j]:
			D[i][j] = D[i - 1][j - 1] + 1
			M[i][j] = 3
		else:
			if D[i - 1][j] >= D[i][j - 1]:
				D[i][j] = D[i - 1][j]
				M[i][j] = 1
			else:
				D[i][j] = D[i][j - 1]
				M[i][j] = 2

print(D[A_len][B_len])
if D[A_len][B_len] != 0:
	result = []
	i, j = A_len, B_len
	while i > 0 and j > 0:
		if A[i] == B[j]:
			result.append(A[i])
		if M[i][j] == 1:
			i -= 1
		elif M[i][j] == 2:
			j -= 1
		else:
			i -= 1
			j -= 1
	result.reverse()
	print(''.join(result))