from sys import stdin


N = int(stdin.readline())
A = [-1] + list(map(int, stdin.readline().split()))
M = int(stdin.readline())
Q = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

# D[i][j] : A[i] ~ A[j]가 팰린드롬인지 여부
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	D[i][i] = 1

for d in range(1, N):
	for i in range(1, N - d + 1):
		s, e = i, i + d
		if s + 1 == e:
			D[s][e] = 1 if A[s] == A[e] else 0
		else:
			D[s][e] = 1 if A[s] == A[e] and D[s + 1][e - 1] == 1 else 0

for q in Q:
	print(D[q[0]][q[1]])