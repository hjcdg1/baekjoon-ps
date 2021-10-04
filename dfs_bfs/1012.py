from sys import stdin
from collections import deque


T = int(stdin.readline())
for _ in range(T):
	M, N, K = list(map(int, stdin.readline().split()))
	XY = [list(map(int, stdin.readline().split())) for _ in range(K)]

	G = [[0 for _ in range(M)] for _ in range(N)]
	for x, y in XY:
		G[y][x] = 1

	visit = [[False for _ in range(M)] for _ in range(N)]
	answer = 0

	for i in range(N):
		for j in range(M):
			if G[i][j] == 1 and not visit[i][j]:
				queue = deque([(i, j)])
				while queue:
					r, c = queue.popleft()
					if visit[r][c]:
						continue

					visit[r][c] = True

					if r > 0 and G[r - 1][c] == 1 and not visit[r - 1][c]:
						queue.append((r - 1, c))
					if c > 0 and G[r][c - 1] == 1 and not visit[r][c - 1]:
						queue.append((r, c - 1))
					if r < N - 1 and G[r + 1][c] == 1 and not visit[r + 1][c]:
						queue.append((r + 1, c))
					if c < M - 1 and G[r][c + 1] == 1 and not visit[r][c + 1]:
						queue.append((r, c + 1))
				answer += 1

	print(answer)
