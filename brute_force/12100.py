from sys import stdin
from copy import deepcopy


def dfs(A, max_block, cnt):
	# 최대 5번만 이동 가능
	if cnt == 5:
		return max_block

	# 왼쪽으로 이동시키는 경우
	A_copy = deepcopy(A)
	is_changed = False
	for i in range(N):
		stack = []
		for j in range(N):
			if A_copy[i][j] == 0:
				continue
			elif stack and stack[-1][0] == A_copy[i][j] and stack[-1][1]:
				stack.pop()
				stack.append((2 * A_copy[i][j], False))
				max_block = max(max_block, 2 * A_copy[i][j])
			else:
				stack.append((A_copy[i][j], True))
		for j in range(N):
			new_num = stack[j][0] if j < len(stack) else 0
			if A_copy[i][j] != new_num:
				A_copy[i][j] = new_num
				is_changed = True
	if not is_changed:
		when_left = max_block
	else:
		when_left = dfs(A_copy, max_block, cnt + 1)

	# 오른쪽으로 이동시키는 경우
	A_copy = deepcopy(A)
	is_changed = False
	for i in range(N):
		stack = []
		for j in reversed(range(N)):
			if A_copy[i][j] == 0:
				continue
			elif stack and stack[-1][0] == A_copy[i][j] and stack[-1][1]:
				stack.pop()
				stack.append((2 * A_copy[i][j], False))
				max_block = max(max_block, 2 * A_copy[i][j])
			else:
				stack.append((A_copy[i][j], True))
		for j in range(N):
			new_num = stack[j][0] if j < len(stack) else 0
			if A_copy[i][N - 1 - j] != new_num:
				A_copy[i][N - 1 - j] = new_num
				is_changed = True
	if not is_changed:
		when_right = max_block
	else:
		when_right = dfs(A_copy, max_block, cnt + 1)

	# 위쪽으로 이동시키는 경우
	A_copy = deepcopy(A)
	is_changed = False
	for j in range(N):
		stack = []
		for i in range(N):
			if A_copy[i][j] == 0:
				continue
			elif stack and stack[-1][0] == A_copy[i][j] and stack[-1][1]:
				stack.pop()
				stack.append((2 * A_copy[i][j], False))
				max_block = max(max_block, 2 * A_copy[i][j])
			else:
				stack.append((A_copy[i][j], True))
		for i in range(N):			
			new_num = stack[i][0] if i < len(stack) else 0
			if A_copy[i][j] != new_num:
				A_copy[i][j] = new_num
				is_changed = True
	if not is_changed:
		when_up = max_block
	else:
		when_up = dfs(A_copy, max_block, cnt + 1)

	# 아래쪽으로 이동시키는 경우
	A_copy = deepcopy(A)
	is_changed = False
	for j in range(N):
		stack = []
		for i in reversed(range(N)):
			if A_copy[i][j] == 0:
				continue
			elif stack and stack[-1][0] == A_copy[i][j] and stack[-1][1]:
				stack.pop()
				stack.append((2 * A_copy[i][j], False))
				max_block = max(max_block, 2 * A_copy[i][j])
			else:
				stack.append((A_copy[i][j], True))
		for i in range(N):
			new_num = stack[i][0] if i < len(stack) else 0
			if A_copy[N - 1 - i][j] != new_num:
				A_copy[N - 1 - i][j] = new_num
				is_changed = True
	if not is_changed:
		when_down = max_block
	else:
		when_down = dfs(A_copy, max_block, cnt + 1)

	return max(when_left, when_right, when_up, when_down)

N = int(stdin.readline())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = dfs(A, max([max(a) for a in A]), 0)
print(answer)
