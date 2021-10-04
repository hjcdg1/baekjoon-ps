from sys import stdin
from collections import deque


N, M, V = list(map(int, stdin.readline().split()))
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]

# 이웃 정점 목록
graph = [[] for _ in range(N + 1)]
for v1, v2 in edges:
	graph[v1].append(v2)
	graph[v2].append(v1)
for v in range(1, N + 1):
	graph[v].sort()

# DFS
stack = [V]
visit = [False for _ in range(N + 1)]
answer = []
while stack:
	v = stack.pop()
	if visit[v]:
		continue

	visit[v] = True
	answer.append(v)

	for nv in reversed(graph[v]):
		if not visit[nv]:
			stack.append(nv)
print(' '.join(map(str, answer)))

# BFS
queue = deque([V])
visit = [False for _ in range(N + 1)]
answer = []
while queue:
	v = queue.popleft()
	if visit[v]:
		continue

	visit[v] = True
	answer.append(v)

	for nv in graph[v]:
		if not visit[nv]:
			queue.append(nv)
print(' '.join(map(str, answer)))
