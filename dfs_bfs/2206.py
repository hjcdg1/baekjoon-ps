from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().split()))
G = [list(stdin.readline().rstrip()) for _ in range(N)]

distance = -1
queue = deque([(0, 0, 1, 0)])

# visit[i][j] == (i, j) 지점에 방문했는가 == (i, j) 지점까지의 최단 거리가 계산되었는가
# visit[i][j][0] : 해당 최단 경로에서 벽을 부순 적이 없는 경우
# visit[i][j][1] : 해당 최단 경로에서 벽을 부순 적이 있는 경우
visit = [[[False, False] for _ in range(M)] for _ in range(N)]

while queue:
	# broken: 벽을 부순 적이 있는 경우 (자기 자신 포함)
	i, j, depth, broken = queue.popleft()
	if visit[i][j][broken]:
		continue

	# (i, j) 지점 방문 완료 == (i, j) 지점까지의 최단 거리 계산 완료
	visit[i][j][broken] = True
	if (i, j) == (N - 1, M - 1):
		distance = depth
		break

	# 벽이 없는 곳(= 0)으로 가는 경로
	if i > 0 and G[i - 1][j] == '0' and not visit[i - 1][j][broken]:
		queue.append((i - 1, j, depth + 1, broken))
	if j > 0 and G[i][j - 1] == '0' and not visit[i][j - 1][broken]:
		queue.append((i, j - 1, depth + 1, broken))
	if i < N - 1 and G[i + 1][j] == '0' and not visit[i + 1][j][broken]:
		queue.append((i + 1, j, depth + 1, broken))
	if j < M - 1 and G[i][j + 1] == '0' and not visit[i][j + 1][broken]:
		queue.append((i, j + 1, depth + 1, broken))

	# 벽이 있는 곳(= 1)으로 가는 경로
	if broken == 0:
		if i > 0 and G[i - 1][j] == '1' and not visit[i - 1][j][1]:
			queue.append((i - 1, j, depth + 1, 1))
		if j > 0 and G[i][j - 1] == '1' and not visit[i][j - 1][1]:
			queue.append((i, j - 1, depth + 1, 1))
		if i < N - 1 and G[i + 1][j] == '1' and not visit[i + 1][j][1]:
			queue.append((i + 1, j, depth + 1, 1))
		if j < M - 1 and G[i][j + 1] == '1' and not visit[i][j + 1][1]:
			queue.append((i, j + 1, depth + 1, 1))

print(distance)
