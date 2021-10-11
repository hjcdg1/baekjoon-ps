from sys import stdin, setrecursionlimit


def get_D(i, j):
	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	if D[i][j] >= 0:
		return D[i][j]

	# D[i][j]의 최초 1회 계산
	else:
		if (i, j) == (M - 1, N - 1):
			D[i][j] = 1
			return D[i][j]

		top, left, bottom, right = 0, 0, 0, 0

		if i > 0 and G[i][j] > G[i - 1][j]:
			top = get_D(i - 1, j)
		if j > 0 and G[i][j] > G[i][j - 1]:
			left = get_D(i, j - 1)
		if i < M - 1 and G[i][j] > G[i + 1][j]:
			bottom = get_D(i + 1, j)
		if j < N - 1 and G[i][j] > G[i][j + 1]:
			right = get_D(i, j + 1)

		D[i][j] = top + left + bottom + right
		return D[i][j]

setrecursionlimit(10000)

M, N = list(map(int, stdin.readline().split()))
G = [list(map(int, stdin.readline().split())) for _ in range(M)]

# D[i][j] : (i, j) 지점에서 출발하여 이동하는 경로의 개수
D = [[-1 for _ in range(N)] for _ in range(M)]

print(get_D(0, 0))
