from sys import stdin


def get_max_distance(v, visit):
	visit[v] = True

	is_leaf = True
	max_d, max_v = 0, None

	for nv, weight in graph[v]:
		if not visit[nv]:
			is_leaf = False
			d, v = get_max_distance(nv, visit)
			if weight + d > max_d:
				max_d = weight + d
				max_v = v

	if is_leaf:
		return 0, v
	else:
		return max_d, max_v

V = int(stdin.readline())
edges = [list(map(int, stdin.readline().split())) for _ in range(V)]

graph = [[] for _ in range(V + 1)]
for edge in edges:
	v1 = edge[0]

	idx = 1
	while edge[idx] != -1:
		v2, weight = edge[idx:idx + 2]
		graph[v1].append((v2, weight))
		idx += 2

# 지름을 구성하는 첫 번째 노드 찾기
visit = [False for _ in range(V + 1)]
_, v1 = get_max_distance(1, visit)

# 지름을 구성하는 두 번째 노드 찾기
visit = [False for _ in range(V + 1)]
d, _ = get_max_distance(v1, visit)

print(d)
