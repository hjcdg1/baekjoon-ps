from sys import stdin


N = int(stdin.readline())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]

heights = set()
for i in range(N):
	for j in range(N):
		heights.add(G[i][j])
heights = sorted(list(heights))
answer = 1

for height in heights:
	visit = [[False for _ in range(N)] for _ in range(N)]
	island_cnt = 0

	for i in range(N):
		for j in range(N):
			if G[i][j] > height and not visit[i][j]:
				stack = [(i, j)]

				while stack:
					r, c = stack.pop()
					if visit[r][c]:
						continue

					visit[r][c] = True

					if r > 0 and G[r - 1][c] > height and not visit[r - 1][c]:
						stack.append((r - 1, c))
					if c > 0 and G[r][c - 1] > height and not visit[r][c - 1]:
						stack.append((r, c - 1))
					if r < N - 1 and G[r + 1][c] > height and not visit[r + 1][c]:
						stack.append((r + 1, c))
					if c < N - 1 and G[r][c + 1] > height and not visit[r][c + 1]:
						stack.append((r, c + 1))

				island_cnt += 1

	answer = max(answer, island_cnt)

print(answer)
