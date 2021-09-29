from sys import stdin


N, M, H = list(map(int, stdin.readline().split()))
horizontal_lines = [list(map(int, stdin.readline().split())) for _ in range(M)]

def left_path_exist(E, pos):
	h, n = pos
	return n > 1 and (n - 1) in E[h]

def right_path_exist(E, pos):
	h, n = pos
	return n < N and n in E[h]

def left_movable(E, pos):
	h, n = pos
	return n > 1 and not (n > 2 and (n - 2) in E[h])

def right_movable(E, pos):
	h, n = pos
	return n < N and not (n < N - 1 and (n + 1) in E[h])

def dfs(E, dst, pos, cnt):
	h, n = pos

	if n > N:
		return True

	for next_h in range(h + 1, H + 1):
		if left_path_exist(E, (next_h, n)):
			return dfs(E, dst, (next_h, n - 1), cnt)

		elif right_path_exist(E, (next_h, n)):
			return dfs(E, dst, (next_h, n + 1), cnt)

		elif cnt > 0:
			if left_movable(E, (next_h, n)):
				E[next_h].append(n - 1)
				if dfs(E, dst, (next_h, n - 1), cnt - 1):
					return True
				else:
					E[next_h].remove(n - 1)

			if right_movable(E, (next_h, n)):
				E[next_h].append(n)
				if dfs(E, dst, (next_h, n + 1), cnt - 1):
					return True
				else:
					E[next_h].remove(n)

	if n == dst:
		return dfs(E, dst + 1, (0, dst + 1), cnt)
	else:
		return False

def simulate(cnt):
	E = [[] for _ in range(H + 1)]
	for horizontal_line in horizontal_lines:
		h, n = horizontal_line
		E[h].append(n)

	return dfs(E, 1, (0, 1), cnt)

def get_answer():
	for cnt in range(4):
		if simulate(cnt):
			return cnt

	return -1

print(get_answer())
