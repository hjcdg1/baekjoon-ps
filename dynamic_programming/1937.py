from sys import stdin, setrecursionlimit

setrecursionlimit(10000)

N = int(stdin.readline())
A = [[0 for _ in range(N + 1)]] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : (i, j)에서 출발할 때 거칠 수 있는 지점의 최대 수
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

def get_D(i, j):
	if D[i][j] == 0:
		max_life = 0
		if i >= 2 and A[i][j] < A[i - 1][j]:
			max_life = max(max_life, get_D(i - 1, j))
		if i <= N - 1 and A[i][j] < A[i + 1][j]:
			max_life = max(max_life, get_D(i + 1, j))
		if j >= 2 and A[i][j] < A[i][j - 1]:
			max_life = max(max_life, get_D(i, j - 1))
		if j <= N - 1 and A[i][j] < A[i][j + 1]:
			max_life = max(max_life, get_D(i, j + 1))
		D[i][j] = max_life + 1
	return D[i][j]

max_D = 0
for i in range(1, N + 1):
	for j in range(1, N + 1):
		max_D = max(max_D, get_D(i, j))
print(max_D)