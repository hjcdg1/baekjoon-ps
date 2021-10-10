from sys import stdin


N = int(stdin.readline())
G = [list(stdin.readline().rstrip()) for _ in range(N)]

answer1 = 0
visit1 = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
	for j in range(N):
		if not visit1[i][j]:
			stack = [(i, j)]

			while stack:
				r, c = stack.pop()
				if visit1[r][c]:
					continue

				visit1[r][c] = True

				if r > 0 and G[r - 1][c] == G[r][c] and not visit1[r - 1][c]:
					stack.append((r - 1, c))
				if c > 0 and G[r][c - 1] == G[r][c] and not visit1[r][c - 1]:
					stack.append((r, c - 1))
				if r < N - 1 and G[r + 1][c] == G[r][c] and not visit1[r + 1][c]:
					stack.append((r + 1, c))
				if c < N - 1 and G[r][c + 1] == G[r][c] and not visit1[r][c + 1]:
					stack.append((r, c + 1))

			answer1 += 1

answer2 = 0
visit2 = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
	for j in range(N):
		if G[i][j] == 'G':
			G[i][j] = 'R'

for i in range(N):
	for j in range(N):
		if not visit2[i][j]:
			stack = [(i, j)]

			while stack:
				r, c = stack.pop()
				if visit2[r][c]:
					continue

				visit2[r][c] = True

				if r > 0 and G[r - 1][c] == G[r][c] and not visit2[r - 1][c]:
					stack.append((r - 1, c))
				if c > 0 and G[r][c - 1] == G[r][c] and not visit2[r][c - 1]:
					stack.append((r, c - 1))
				if r < N - 1 and G[r + 1][c] == G[r][c] and not visit2[r + 1][c]:
					stack.append((r + 1, c))
				if c < N - 1 and G[r][c + 1] == G[r][c] and not visit2[r][c + 1]:
					stack.append((r, c + 1))

			answer2 += 1

print('{} {}'.format(answer1, answer2))
