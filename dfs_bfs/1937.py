from sys import stdin, setrecursionlimit


def get_D(i, j):
	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	if D[i][j] > 0:
		return D[i][j]

	# D[i][j]의 최초 1회 계산
	else:
		cnt = 1

		if i > 0 and G[i - 1][j] > G[i][j]:
			cnt = max(cnt, get_D(i - 1, j) + 1)
		if j > 0 and G[i][j - 1] > G[i][j]:
			cnt = max(cnt, get_D(i, j - 1) + 1)
		if i < N - 1 and G[i + 1][j] > G[i][j]:
			cnt = max(cnt, get_D(i + 1, j) + 1)
		if j < N - 1 and G[i][j + 1] > G[i][j]:
			cnt = max(cnt, get_D(i, j + 1) + 1)

		D[i][j] = cnt
		return D[i][j]

setrecursionlimit(10000)

N = int(stdin.readline())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][j] : (i, j) 지점에서 출발하여 이동하는 경로의 최대 길이
D = [[0 for _ in range(N)] for _ in range(N)]

answer = 0
for i in range(N):
	for j in range(N):
		answer = max(answer, get_D(i, j))

print(answer)
