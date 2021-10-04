from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().split()))
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for v1, v2 in edges:
	graph[v1].append(v2)
	graph[v2].append(v1)

visit = [False for _ in range(N + 1)]
answer = 0

for i in range(1, N + 1):
	if not visit[i]:
		queue = deque([i])
		while queue:
			v = queue.popleft()
			if visit[v]:
				continue

			visit[v] = True

			for nv in graph[v]:
				if not visit[nv]:
					queue.append(nv)
		answer +=1

print(answer)
