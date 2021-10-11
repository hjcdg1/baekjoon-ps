from sys import stdin
from collections import deque


def is_bipartite(V, graph):
	visit = [False for _ in range(V + 1)]
	groups = [None for _ in range(V + 1)]

	for i in range(1, V + 1):
		if not visit[i]:
			groups[i] = 0
			queue = deque([i])

			while queue:
				v = queue.popleft()
				if visit[v]:
					continue

				visit[v] = True

				for nv in graph[v]:
					if not visit[nv]:
						new_group = 0 if groups[v] == 1 else 1
						if groups[nv] is not None and groups[nv] != new_group:
							return 'NO'
						else:
							groups[nv] = new_group

						queue.append(nv)

	return 'YES'

K = int(stdin.readline())
for _ in range(K):
	V, E = list(map(int, stdin.readline().split()))
	edges = [list(map(int, stdin.readline().split())) for _ in range(E)]

	graph = [[] for _ in range(V + 1)]
	for v1, v2 in edges:
		graph[v1].append(v2)
		graph[v2].append(v1)

	print(is_bipartite(V, graph))
