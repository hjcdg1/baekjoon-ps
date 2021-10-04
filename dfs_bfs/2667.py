from sys import stdin
from collections import deque


N = int(stdin.readline())
G = [list(stdin.readline().rstrip()) for _ in range(N)]

visit = [[False for _ in range(N)] for _ in range(N)]
cnt_list = []

for i in range(N):
	for j in range(N):
		if G[i][j] == '1' and not visit[i][j]:
			queue = deque([(i, j)])
			cnt = 0

			while queue:
				r, c = queue.popleft()
				if visit[r][c]:
					continue

				visit[r][c] = True
				cnt += 1

				if r > 0 and G[r - 1][c] == '1' and not visit[r - 1][c]:
					queue.append((r - 1, c))
				if c > 0 and G[r][c - 1] == '1' and not visit[r][c - 1]:
					queue.append((r, c - 1))
				if r < N - 1 and G[r + 1][c] == '1' and not visit[r + 1][c]:
					queue.append((r + 1, c))
				if c < N - 1 and G[r][c + 1] == '1' and not visit[r][c + 1]:
					queue.append((r, c + 1))

			cnt_list.append(cnt)

print(len(cnt_list))
for cnt in sorted(cnt_list):
	print(cnt)
