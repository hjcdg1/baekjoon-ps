from sys import stdin


N = int(stdin.readline())
A = [0] + list(map(int, stdin.readline().split()))
M = int(stdin.readline())
Q = [list(map(int, stdin.readline().split())) for _ in range(M)]

# D[i][j] : A[i] ~ A[j]가 팰린드롬인지 여부
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	D[i][i] = 1

for i in range(1, N):
	D[i][i + 1] = 1 if A[i] == A[i + 1] else 0

for d in range(2, N):
	for i in range(1, N - d + 1):
		start = i
		end = i + d
		D[start][end] = D[start + 1][end - 1] if A[start] == A[end] else 0

for q in Q:
	print(D[q[0]][q[1]])
