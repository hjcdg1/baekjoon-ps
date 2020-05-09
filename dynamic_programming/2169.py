from sys import stdin, setrecursionlimit


setrecursionlimit(1000000)

N, M = tuple(map(int, stdin.readline().split()))
A = [[0 for _ in range(M + 1)]] + [[0] + list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j][src] : A[i][j]에서 출발할 때 가치 합의 최댓값 (src: 온 방향)
D = [[[0, 0, 0] for _ in range(M + 1)] for _ in range(N + 1)]
visited = [[[False, False, False] for _ in range(M + 1)] for _ in range(N + 1)]

def get_D(i, j, src):
	if visited[i][j][src]:
		return D[i][j][src]
	else:
		if i == N and j == M:
			D[i][j][src] = A[i][j]
		else:
			max_D = float('-inf')

			if src == 0:
				if i + 1 <= N:
					max_D = max(max_D, get_D(i + 1, j, 1))
				if j + 1 <= M:
					max_D = max(max_D, get_D(i, j + 1, 0))
			elif src == 1:
				if j - 1 >= 1:
					max_D = max(max_D, get_D(i, j - 1, 2))
				if i + 1 <= N:
					max_D = max(max_D, get_D(i + 1, j, 1))
				if j + 1 <= M:
					max_D = max(max_D, get_D(i, j + 1, 0))
			else:
				if j - 1 >= 1:
					max_D = max(max_D, get_D(i, j - 1, 2))
				if i + 1 <= N:
					max_D = max(max_D, get_D(i + 1, j, 1))
			D[i][j][src] = max_D + A[i][j]

		visited[i][j][src] = True
		return D[i][j][src]

print(get_D(1, 1, 0))