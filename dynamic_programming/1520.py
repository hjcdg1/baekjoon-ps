# Try again

from sys import stdin, setrecursionlimit


setrecursionlimit(10000)

M, N = tuple(map(int, stdin.readline().split()))
A = [[0 for _ in range(N + 1)]] + [[0] + list(map(int, stdin.readline().split())) for _ in range(M)]

# D[i][j] : (i, j)에서 출발할 때의 답
D = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
V = [[False for _ in range(N + 1)] for _ in range(M + 1)]

def getD(i, j):
	# 도착점
	if i == M and j == N:
		return 1

	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	elif V[i][j]:
		return D[i][j]

	# D[i][j]의 최초 1회 계산
	else:
		if j >= 2 and A[i][j - 1] < A[i][j]:
			D[i][j] += getD(i, j - 1)
		if j <= N - 1 and A[i][j + 1] < A[i][j]:
			D[i][j] += getD(i, j + 1)
		if i >= 2 and A[i - 1][j] < A[i][j]:
			D[i][j] += getD(i - 1, j)
		if i <= M - 1 and A[i + 1][j] < A[i][j]:
			D[i][j] += getD(i + 1, j)
		V[i][j] = True
		return D[i][j]

print(getD(1, 1))