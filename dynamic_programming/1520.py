from sys import stdin, setrecursionlimit


setrecursionlimit(10000)

M, N = list(map(int, stdin.readline().split()))
A = [None] + [[None] + list(map(int, stdin.readline().split())) for _ in range(M)]

# D[i][j] : (i, j) 지점까지 내리막길로만 이동하는 경로의 개수
D = [None] + [[None] + [0 for _ in range(N)] for _ in range(M)]

# V[i][j] : D[i][j] 값의 계산 완료 여부
V = [None] + [[None] + [False for _ in range(N)] for _ in range(M)]

def get_D(i, j):
	# 출발점
	if i == 1 and j == 1:
		return 1

	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	elif V[i][j]:
		return D[i][j]

	# D[i][j]의 최초 1회 계산
	else:
		if i >= 2 and A[i][j] < A[i - 1][j]:
			D[i][j] += get_D(i - 1, j)
		if i <= M - 1 and A[i][j] < A[i + 1][j]:
			D[i][j] += get_D(i + 1, j)
		if j >= 2 and A[i][j] < A[i][j - 1]:
			D[i][j] += get_D(i, j - 1)
		if j <= N - 1 and A[i][j] < A[i][j + 1]:
			D[i][j] += get_D(i, j + 1)
		V[i][j] = True
		return D[i][j]

print(get_D(M, N))
