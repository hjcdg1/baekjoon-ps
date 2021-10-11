from sys import stdin
from collections import deque


N = int(stdin.readline())
A, B = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for v1, v2 in edges:
	graph[v1].append(v2)
	graph[v2].append(v1)

queue = deque([(A, 0)])
visit = [False for _ in range(N + 1)]

while queue:
	v, depth = queue.popleft()
	# 트리이기 때문에 v의 방문 여부를 여기서 검사할 필요가 없음.

	visit[v] = True
	if v == B:
		print(depth)
		exit(0)

	for nv in graph[v]:
		if not visit[nv]:
			queue.append((nv, depth + 1))

print(-1)
