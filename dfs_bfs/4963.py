from sys import stdin


while True:
	W, H = list(map(int, stdin.readline().split()))
	if (W, H) == (0, 0):
		break
	G = [list(map(int, stdin.readline().split())) for _ in range(H)]

	visit = [[False for _ in range(W)] for _ in range(H)]
	answer = 0

	for i in range(H):
		for j in range(W):
			if G[i][j] == 1 and not visit[i][j]:
				stack = [(i, j)]

				while stack:
					r, c = stack.pop()
					if visit[r][c]:
						continue

					visit[r][c] = True

					if r > 0 and G[r - 1][c] == 1 and not visit[r - 1][c]:
						stack.append((r - 1, c))
					if r > 0 and c < W - 1 and G[r - 1][c + 1] == 1 and not visit[r - 1][c + 1]:
						stack.append((r - 1, c + 1))
					if c < W - 1 and G[r][c + 1] == 1 and not visit[r][c + 1]:
						stack.append((r, c + 1))
					if r < H - 1 and c < W - 1 and G[r + 1][c + 1] == 1 and not visit[r + 1][c + 1]:
						stack.append((r + 1, c + 1))
					if r < H - 1 and G[r + 1][c] == 1 and not visit[r + 1][c]:
						stack.append((r + 1, c))
					if r < H - 1 and c > 0 and G[r + 1][c - 1] == 1 and not visit[r + 1][c - 1]:
						stack.append((r + 1, c - 1))
					if c > 0 and G[r][c - 1] == 1 and not visit[r][c - 1]:
						stack.append((r, c - 1))
					if r > 0 and c > 0 and G[r - 1][c - 1] == 1 and not visit[r - 1][c - 1]:
						stack.append((r - 1, c - 1))

				answer += 1

	print(answer)
