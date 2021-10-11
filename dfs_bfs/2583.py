from sys import stdin


M, N, K = list(map(int, stdin.readline().split()))
R =[list(map(int, stdin.readline().split())) for _ in range(K)]

G = [[0 for _ in range(N)] for _ in range(M)]

for x1, y1, x2, y2 in R:
	# 왼쪽 위 : (y1, x1)
	# 오른쪽 아래 : (y2 - 1, x2 - 1)
	for i in range(y1, y2):
		for j in range(x1, x2):
			G[i][j] = 1

visit = [[False for _ in range(N)] for _ in range(M)]
group_cnt = 0
group_areas = []

for i in range(M):
	for j in range(N):
		if G[i][j] == 0 and not visit[i][j]:
			stack = [(i, j)]
			group_area = 0

			while stack:
				r, c = stack.pop()
				if visit[r][c]:
					continue

				visit[r][c] = True
				group_area += 1

				if r > 0 and G[r - 1][c] == 0 and not visit[r - 1][c]:
					stack.append((r - 1, c))
				if c > 0 and G[r][c - 1] == 0 and not visit[r][c - 1]:
					stack.append((r, c - 1))
				if r < M - 1 and G[r + 1][c] == 0 and not visit[r + 1][c]:
					stack.append((r + 1, c))
				if c < N - 1 and G[r][c + 1] == 0 and not visit[r][c + 1]:
					stack.append((r, c + 1))

			group_cnt += 1
			group_areas.append(group_area)

print(group_cnt)
print(' '.join(map(str, sorted(group_areas))))
