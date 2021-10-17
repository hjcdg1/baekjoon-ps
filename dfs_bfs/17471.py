from sys import stdin
from itertools import product
from collections import deque


def bfs(i):
	# 시작 노드의 그룹
	group = permutation[i]

	# 시작 노드 방문
	queue = deque([i])
	visit[i] = True
	group_cnt[group] -= 1	
	if group_cnt[group] == 0:
		return True

	while queue:
		v = queue.popleft()
		for nv in graph[v]:
			if not visit[nv] and permutation[nv] == group:
				queue.append(nv)
				visit[nv] = True
				group_cnt[group] -= 1
				if group_cnt[group] == 0:
					return True
	return False

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

graph = [[] for _ in range(N)]
for v, a in enumerate(A):
	for nv in a[1:]:
		graph[v].append(nv - 1)

min_diff = float('inf')
for permutation in product([0, 1], repeat=N):
	# 두 그룹의 노드 개수 계산
	group_cnt = [0, 0]
	for group in permutation:
		group_cnt[group] += 1
	if group_cnt[0] == 0 or group_cnt[1] == 0:
		continue

	# BFS
	visit = [False for _ in range(N)]
	is_correct = True
	for i in range(N):
		if not visit[i] and not bfs(i):
			is_correct = False
			break

	# 그룹을 올바르게 나눈 경우, 두 그룹의 인구수 차이 계산
	if is_correct:
		group_population = [0, 0]
		for v, group in enumerate(permutation):
			group_population[group] += P[v]
		diff = abs(group_population[0] - group_population[1])
		min_diff = min(min_diff, diff)

print(min_diff if min_diff != float('inf') else -1)
