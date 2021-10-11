from sys import stdin


N = int(stdin.readline())
edges = [list(map(int, stdin.readline().split())) for _ in range(N - 1)]

graph = [[] for _ in range(N + 1)]
for v1, v2 in edges:
	graph[v1].append(v2)
	graph[v2].append(v1)

stack = [(1, 0)]
visit = [False for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

while stack:
	v, parent = stack.pop()
	# 트리이기 때문에 v의 방문 여부를 여기서 검사할 필요가 없음.

	visit[v] = True
	parents[v] = parent

	for nv in graph[v]:
		if not visit[nv]:
			stack.append((nv, v))

for parent in parents[2:]:
	print(parent)
