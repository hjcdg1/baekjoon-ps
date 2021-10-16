from sys import stdin
from collections import deque


N, M = list(map(int, stdin.readline().split()))
edges = [list(map(int, stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for v1, v2 in edges:
	graph[v2].append(v1)

cnt_info_list = []
for i in range(1, N + 1):
	queue = deque()
	visit = [False for _ in range(N + 1)]
	cnt = 0

	queue.append(i)
	visit[i] = True
	cnt += 1

	while queue:
		v = queue.popleft()
		for nv in graph[v]:
			if not visit[nv]:
				queue.append(nv)
				visit[nv] = True
				cnt += 1

	cnt_info_list.append({'cnt': cnt, 'node': i})

max_cnt = max([cnt_info['cnt'] for cnt_info in cnt_info_list])
answer = [
	cnt_info['node']
	for cnt_info in cnt_info_list
	if cnt_info['cnt'] == max_cnt
]
print(*answer)
