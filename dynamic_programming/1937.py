from sys import stdin, setrecursionlimit


setrecursionlimit(10000)

N = int(stdin.readline())
A = [None] + [[None] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : (i, j) 지점에서 출발할 때 거칠 수 있는 지점의 최대 개수
D = [None] + [[None] + [0 for _ in range(N)] for _ in range(N)]

# V[i][j] : D[i][j] 값의 계산 완료 여부
V = [None] + [[None] + [False for _ in range(N)] for _ in range(N)]

def get_D(i, j):
	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	if V[i][j]:
		return D[i][j]

	# D[i][j]의 최초 1회 계산
	else:
		D[i][j] = 1
		if i >= 2 and A[i - 1][j] > A[i][j]:
			D[i][j] = max(D[i][j], get_D(i - 1, j) + 1)
		if i <= N - 1 and A[i + 1][j] > A[i][j]:
			D[i][j] = max(D[i][j], get_D(i + 1, j) + 1)
		if j >= 2 and A[i][j - 1] > A[i][j]:
			D[i][j] = max(D[i][j], get_D(i, j - 1) + 1)
		if j <= N - 1 and A[i][j + 1] > A[i][j]:
			D[i][j] = max(D[i][j], get_D(i, j + 1) + 1)
		V[i][j] = True
		return D[i][j]

max_D = 0
for i in range(1, N + 1):
	for j in range(1, N + 1):
		max_D = max(max_D, get_D(i, j))
print(max_D)
