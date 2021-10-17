from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().split()))
G = [list(map(int, stdin.readline().split())) for _ in range(N)]

total_cheeze_cnt = 0
for i in range(N):
	for j in range(M):
		if G[i][j] == 1:
			total_cheeze_cnt += 1

hours = 0
while total_cheeze_cnt > 0:
	queue = deque()
	visit = [[False for _ in range(M)] for _ in range(N)]
	count = [[0 for _ in range(M)] for _ in range(N)]
	delete = []

	queue.append((0, 0))
	visit[0][0] = True

	while queue:
		i, j = queue.popleft()

		if i > 0:
			if G[i - 1][j] == 1:
				count[i - 1][j] += 1
				if count[i - 1][j] == 2:
					delete.append((i - 1, j))
			elif G[i - 1][j] == 0 and not visit[i - 1][j]:
				queue.append((i - 1, j))
				visit[i - 1][j] = True
		if j > 0:
			if G[i][j - 1] == 1:
				count[i][j - 1] += 1
				if count[i][j - 1] == 2:
					delete.append((i, j - 1))
			elif G[i][j - 1] == 0 and not visit[i][j - 1]:
				queue.append((i, j - 1))
				visit[i][j - 1] = True
		if i < N - 1:
			if G[i + 1][j] == 1:
				count[i + 1][j] += 1
				if count[i + 1][j] == 2:
					delete.append((i + 1, j))
			elif G[i + 1][j] == 0 and not visit[i + 1][j]:
				queue.append((i + 1, j))
				visit[i + 1][j] = True
		if j < M - 1:
			if G[i][j + 1] == 1:
				count[i][j + 1] += 1
				if count[i][j + 1] == 2:
					delete.append((i, j + 1))
			elif G[i][j + 1] == 0 and not visit[i][j + 1]:
				queue.append((i, j + 1))
				visit[i][j + 1] = True

	for i, j in delete:
		G[i][j] = 0
		total_cheeze_cnt -= 1

	hours += 1

print(hours)
