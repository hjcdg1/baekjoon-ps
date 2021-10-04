from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().split()))
G = [list(stdin.readline().rstrip()) for _ in range(N)]

queue = deque([(0, 0, 1)])
visit = [[False for _ in range(M)] for _ in range(N)]

while queue:
	i, j, depth = queue.popleft()
	if visit[i][j]:
		continue

	visit[i][j] = True

	if (i, j) == (N - 1, M - 1):
		print(depth)
		exit(0)

	if i > 0 and G[i - 1][j] == '1' and not visit[i - 1][j]:
		queue.append((i - 1, j, depth + 1))
	if j > 0 and G[i][j - 1] == '1' and not visit[i][j - 1]:
		queue.append((i, j - 1, depth + 1))
	if i < N - 1 and G[i + 1][j] == '1' and not visit[i + 1][j]:
		queue.append((i + 1, j, depth + 1))
	if j < M - 1 and G[i][j + 1] == '1' and not visit[i][j + 1]:
		queue.append((i, j + 1, depth + 1))
