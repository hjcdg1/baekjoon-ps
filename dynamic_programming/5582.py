from sys import stdin


A = [None] + list(stdin.readline().rstrip())
B = [None] + list(stdin.readline().rstrip())

A_len = len(A) - 1
B_len = len(B) - 1

# D[i][j] : A[i]와 B[j]를 끝으로 하는 가장 긴 공통 부분 문자열의 길이
D = [[0 for _ in range(B_len + 1)] for _ in range(A_len + 1)]

for i in range(1, A_len + 1):
	for j in range(1, B_len + 1):
		if A[i] == B[j]:
			D[i][j] = D[i - 1][j - 1] + 1

max_D = -1
for i in range(1, A_len + 1):
	for j in range(1, B_len + 1):
		max_D = max(max_D, D[i][j])

print(max_D)