from sys import stdin
from collections import deque


N, K = list(map(int, stdin.readline().split()))

queue = deque([(N, 0)])
visit = [False for _ in range(200000)]

while queue:
	v, depth = queue.popleft()
	if visit[v]:
		continue

	visit[v] = True
	if v == K:
		print(depth)
		break

	if v > 0 and not visit[v - 1]:
		queue.append((v - 1, depth + 1))
	if v < K and not visit[v + 1]:
		queue.append((v + 1, depth + 1))
	if v < K and not visit[2 * v]:
		queue.append((2 * v, depth + 1))
