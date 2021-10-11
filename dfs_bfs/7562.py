from sys import stdin
from collections import deque


T = int(stdin.readline())
for _ in range(T):
	I = int(stdin.readline())
	S = list(map(int, stdin.readline().split()))
	D = list(map(int, stdin.readline().split()))

	queue = deque([(S[0], S[1], 0)])
	visit = [[False for _ in range(I)] for _ in range(I)]

	while queue:
		i, j, depth = queue.popleft()
		if visit[i][j]:
			continue

		visit[i][j] = True
		if (i, j) == tuple(D):
			print(depth)
			break

		if i > 1 and j > 0 and not visit[i - 2][j - 1]:
			queue.append((i - 2, j - 1, depth + 1))
		if i > 0 and j > 1 and not visit[i - 1][j - 2]:
			queue.append((i - 1, j - 2, depth + 1))
		if i < I - 1 and j > 1 and not visit[i + 1][j - 2]:
			queue.append((i + 1, j - 2, depth + 1))
		if i < I - 2 and j > 0 and not visit[i + 2][j - 1]:
			queue.append((i + 2, j - 1, depth + 1))
		if i < I - 2 and j < I - 1 and not visit[i + 2][j + 1]:
			queue.append((i + 2, j + 1, depth + 1))
		if i < I - 1 and j < I - 2 and not visit[i + 1][j + 2]:
			queue.append((i + 1, j + 2, depth + 1))
		if i > 0 and j < I - 2 and not visit[i - 1][j + 2]:
			queue.append((i - 1, j + 2, depth + 1))
		if i > 1 and j < I - 1 and not visit[i - 2][j + 1]:
			queue.append((i - 2, j + 1, depth + 1))
