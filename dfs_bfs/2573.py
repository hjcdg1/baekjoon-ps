from sys import stdin
from copy import deepcopy


def get_G_after_1year(G):
	new_G = deepcopy(G)
	for i in range(N):
		for j in range(M):
			if G[i][j] > 0:
				if i > 0 and G[i - 1][j] == 0:
					new_G[i][j] -= 1
				if j > 0 and G[i][j - 1] == 0:
					new_G[i][j] -= 1
				if i < N - 1 and G[i + 1][j] == 0:
					new_G[i][j] -= 1
				if j < M - 1 and G[i][j + 1] == 0:
					new_G[i][j] -= 1
				new_G[i][j] = max(new_G[i][j], 0)
	return new_G

def get_group_cnt(G):
	visit = [[False for _ in range(M)] for _ in range(N)]
	group_cnt = 0

	for i in range(N):
		for j in range(M):
			if G[i][j] > 0 and not visit[i][j]:
				stack = [(i, j)]

				while stack:
					r, c = stack.pop()
					if visit[r][c]:
						continue

					visit[r][c] = True

					if r > 0 and G[r - 1][c] > 0 and not visit[r - 1][c]:
						stack.append((r - 1, c))
					if c > 0 and G[r][c - 1] > 0 and not visit[r][c - 1]:
						stack.append((r, c - 1))
					if r < N - 1 and G[r + 1][c] > 0 and not visit[r + 1][c]:
						stack.append((r + 1, c))
					if c < M - 1 and G[r][c + 1] > 0 and not visit[r][c + 1]:
						stack.append((r, c + 1))

				group_cnt += 1

	return group_cnt

N, M = list(map(int, stdin.readline().split()))
G = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 처음부터 빙산이 두 덩어리 이상인 경우
if get_group_cnt(G) >= 2:
	print(0)

# 그렇지 않은 경우 (최소 1년 이상의 시간이 흘러야 하는 경우)
else:
	year = 0

	while True:
		year += 1
		G = get_G_after_1year(G)
		group_cnt = get_group_cnt(G)

		# 전부 다 녹은 경우
		if group_cnt == 0:
			print(0)
			break

		# 빙산이 두 덩어리 이상이 된 경우
		if group_cnt >= 2:
			print(year)
			break
