from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().split()))
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]

graph = [set() for _ in range(N + 1)]
for v1, v2 in edges:
	graph[v1].add(v2)
	graph[v2].add(v1)

min_kevin = float('inf')
answer = None

for i in range(1, N + 1):
	queue = deque()
	visit = [False for _ in range(N + 1)]
	steps = [0 for _ in range(N + 1)]

	queue.append((i, 0))
	visit[i] = True

	while queue:
		v, depth = queue.popleft()
		for nv in graph[v]:
			if not visit[nv]:
				queue.append((nv, depth + 1))
				visit[nv] = True
				steps[nv] = depth + 1

	kevin = sum(steps[1:])
	if kevin < min_kevin:
		min_kevin = kevin
		answer = i

print(answer)
