from sys import stdin, setrecursionlimit


"""
트리의 지름은 가장 긴 경로의 길이로 정의된다.
임의의 한 노드와 가장 멀리 떨어진 노드는 반드시
지름을 구성하는 두 노드 중에 하나가 된다.
"""

def get_farthest_node(v, visit):
	visit[v] = True

	result = {'num': v, 'distance': 0}
	for nv, weight in graph[v]:
		if not visit[nv]:
			farthest_node = get_farthest_node(nv, visit)
			if weight + farthest_node['distance'] > result['distance']:
				result['num'] = farthest_node['num']
				result['distance'] = weight + farthest_node['distance']

	return result

setrecursionlimit(100000)

N = int(stdin.readline())
edges = [list(map(int, stdin.readline().split())) for _ in range(N - 1)]

graph = [[] for _ in range(N + 1)]
for v1, v2, weight in edges:
	graph[v1].append((v2, weight))
	graph[v2].append((v1, weight))

visit = [False for _ in range(N + 1)]
v1_info = get_farthest_node(1, visit)

visit = [False for _ in range(N + 1)]
v2_info = get_farthest_node(v1_info['num'], visit)

print(v2_info['distance'])
