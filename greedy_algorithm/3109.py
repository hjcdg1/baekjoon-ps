# Try again

import sys


R, C = tuple(map(int, sys.stdin.readline().split()))
G = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

cnt = 0
for i in range(R):
	arrive = False
	
	stack = []
	stack.append((i, 0))
	while stack:
		# 살펴볼 위치 pop
		r, c = stack.pop()
		G[r][c] = 'x'

		# 도착
		if c == C - 1:
			arrive = True
			break

		# 방문 가능한 자식 스택에 push
		if r + 1 < R and c + 1 < C and G[r + 1][c + 1] != 'x':
			stack.append((r + 1, c + 1))
		if c + 1 < C and G[r][c + 1] != 'x':
			stack.append((r, c + 1))
		if r - 1 >= 0 and c + 1 < C and G[r - 1][c + 1] != 'x':
			stack.append((r - 1, c + 1))

	if arrive:
		cnt += 1

print(cnt)