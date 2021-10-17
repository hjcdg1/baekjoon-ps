from sys import stdin
from collections import deque


R, C = list(map(int, stdin.readline().split()))
G = [list(stdin.readline().rstrip()) for _ in range(R)]

w_list = []
d, s = None, None
for i in range(R):
	for j in range(C):
		if G[i][j] == '*':
			w_list.append((i, j))
		elif G[i][j] == 'D':
			d = (i, j)
		elif G[i][j] == 'S':
			s = (i, j)
			G[i][j] = '.'

# 물의 전파에 대한 큐
curr_queue_w = deque()
visit_w = [[False for _ in range(C)] for _ in range(R)]
for w in w_list:
	curr_queue_w.append((w[0], w[1]))
	visit_w[w[0]][w[1]] = True

# 고슴도치의 이동에 대한 큐
curr_queue_s = deque()
visit_s = [[False for _ in range(C)] for _ in range(R)]
curr_queue_s.append((s[0], s[1]))
visit_s[s[0]][s[1]] = True

curr_depth = 0
while True:
	next_queue_w = deque()
	while curr_queue_w:
		i, j = curr_queue_w.popleft()
		if i > 0 and G[i - 1][j] == '.' and not visit_w[i - 1][j]:
			G[i - 1][j] = '*'
			next_queue_w.append((i - 1, j))
			visit_w[i - 1][j] = True
		if j > 0 and G[i][j - 1] == '.' and not visit_w[i][j - 1]:
			G[i][j - 1] = '*'
			next_queue_w.append((i, j - 1))
			visit_w[i][j - 1] = True
		if i < R - 1 and G[i + 1][j] == '.' and not visit_w[i + 1][j]:
			G[i + 1][j] = '*'
			next_queue_w.append((i + 1, j))
			visit_w[i + 1][j] = True
		if j < C - 1 and G[i][j + 1] == '.' and not visit_w[i][j + 1]:
			G[i][j + 1] = '*'
			next_queue_w.append((i, j + 1))
			visit_w[i][j + 1] = True
	if next_queue_w:
		curr_queue_w = next_queue_w

	next_queue_s = deque()
	while curr_queue_s:
		i, j = curr_queue_s.popleft()
		if G[i][j] == 'D':
			print(curr_depth)
			exit(0)
		if i > 0 and G[i - 1][j] in ('.', 'D') and not visit_s[i - 1][j]:
			next_queue_s.append((i - 1, j))
			visit_s[i - 1][j] = True
		if j > 0 and G[i][j - 1] in ('.', 'D') and not visit_s[i][j - 1]:
			next_queue_s.append((i, j - 1))
			visit_s[i][j - 1] = True
		if i < R - 1 and G[i + 1][j] in ('.', 'D') and not visit_s[i + 1][j]:
			next_queue_s.append((i + 1, j))
			visit_s[i + 1][j] = True
		if j < C - 1 and G[i][j + 1] in ('.', 'D') and not visit_s[i][j + 1]:
			next_queue_s.append((i, j + 1))
			visit_s[i][j + 1] = True
	if next_queue_s:
		curr_queue_s = next_queue_s

	if next_queue_w or next_queue_s:
		curr_depth += 1
	else:
		break

print('KAKTUS')
