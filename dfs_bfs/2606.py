from sys import stdin
from collections import deque


V = int(stdin.readline())
E = int(stdin.readline())
edges = [list(map(int, stdin.readline().split())) for _ in range(E)]

graph = [[] for _ in range(V + 1)]
for v1, v2 in edges:
	graph[v1].append(v2)
	graph[v2].append(v1)

queue = deque([1])
visit = [False for _ in range(V + 1)]
cnt = 0

while queue:
	v = queue.popleft()
	if visit[v]:
		continue

	visit[v] = True
	cnt += 1

	for nv in graph[v]:
		if not visit[nv]:
			queue.append(nv)

print(cnt - 1)
