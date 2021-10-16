from sys import stdin


def is_movable(r_pos, b_pos, direction):
	r_i, r_j = r_pos
	b_i, b_j = b_pos

	if direction == 'up':
		if r_i <= b_i:
			return G[r_i - 1][r_j] in ('.', 'O') or (
				G[b_i - 1][b_j] in ('.', 'O') and (b_i - 1, b_j) != (r_i, r_j)
			)
		else:
			return G[b_i - 1][b_j] in ('.', 'O') or (
				G[r_i - 1][r_j] in ('.', 'O') and (r_i - 1, r_j) != (b_i, b_j)
			)
	elif direction == 'left':
		if r_j <= b_j:
			return G[r_i][r_j - 1] in ('.', 'O') or (
				G[b_i][b_j - 1] in ('.', 'O') and (b_i, b_j - 1) != (r_i, r_j)
			)
		else:
			return G[b_i][b_j - 1] in ('.', 'O') or (
				G[r_i][r_j - 1] in ('.', 'O') and (r_i, r_j - 1) != (b_i, b_j)
			)
	elif direction == 'down':
		if b_i <= r_i:
			return G[r_i + 1][r_j] in ('.', 'O') or (
				G[b_i + 1][b_j] in ('.', 'O') and (b_i + 1, b_j) != (r_i, r_j)
			)
		else:
			return G[b_i + 1][b_j] in ('.', 'O') or (
				G[r_i + 1][r_j] in ('.', 'O') and (r_i + 1, r_j) != (b_i, b_j)
			)
	else:
		if b_j <= r_j:
			return G[r_i][r_j + 1] in ('.', 'O') or (
				G[b_i][b_j + 1] in ('.', 'O') and (b_i, b_j + 1) != (r_i, r_j)
			)
		else:
			return G[b_i][b_j + 1] in ('.', 'O') or (
				G[r_i][r_j + 1] in ('.', 'O') and (r_i, r_j + 1) != (b_i, b_j)
			)

def move_ball(x_pos, y_pos, direction):
	x_i, x_j = x_pos
	y_i, y_j = y_pos

	if direction == 'up':
		while True:
			if G[x_i - 1][x_j] == '.' and (x_i - 1, x_j) != (y_i, y_j):
				x_i -= 1
			else:
				if G[x_i - 1][x_j] == 'O':
					x_i, x_j = None, None
				break
	elif direction == 'left':
		while True:
			if G[x_i][x_j - 1] == '.' and (x_i, x_j - 1) != (y_i, y_j):
				x_j -= 1
			else:
				if G[x_i][x_j - 1] == 'O':
					x_i, x_j = None, None
				break
	elif direction == 'down':
		while True:
			if G[x_i + 1][x_j] == '.' and (x_i + 1, x_j) != (y_i, y_j):
				x_i += 1
			else:
				if G[x_i + 1][x_j] == 'O':
					x_i, x_j = None, None
				break
	else:
		while True:
			if G[x_i][x_j + 1] == '.' and (x_i, x_j + 1) != (y_i, y_j):
				x_j += 1
			else:
				if G[x_i][x_j + 1] == 'O':
					x_i, x_j = None, None
				break

	return x_i, x_j

def move(r_pos, b_pos, direction):
	r_i, r_j = r_pos
	b_i, b_j = b_pos

	if direction == 'up':
		if r_i <= b_i:
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
		else:
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
	elif direction == 'left':
		if r_j <= b_j:
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
		else:
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
	elif direction == 'down':
		if b_i <= r_i:
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
		else:
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
	else:
		if b_j <= r_j:
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
		else:
			b_i, b_j = move_ball((b_i, b_j), (r_i, r_j), direction)
			r_i, r_j = move_ball((r_i, r_j), (b_i, b_j), direction)

	return (r_i, r_j), (b_i, b_j)

def get_answer(r_pos, b_pos, cnt):
	if cnt == 10:
		return float('inf')

	answer = float('inf')
	for direction in ['up', 'left', 'down', 'right']:
		if is_movable(r_pos, b_pos, direction):
			new_r_pos, new_b_pos = move(r_pos, b_pos, direction)
			# print(new_r_pos, new_b_pos, cnt + 1)
			if new_b_pos[0] is None:
				continue
			elif new_r_pos[0] is None:
				return cnt + 1
			else:
				answer = min(answer, get_answer(new_r_pos, new_b_pos, cnt + 1))

	return answer

N, M = list(map(int, stdin.readline().split()))
G = [list(stdin.readline().rstrip()) for _ in range(N)]

# 빨간 공과 파란 공의 위치
R_pos, B_pos = None, None
for i in range(N):
	for j in range(M):
		if G[i][j] == 'R':
			G[i][j] = '.'
			R_pos = (i, j)
		elif G[i][j] == 'B':
			G[i][j] = '.'
			B_pos = (i, j)

answer = get_answer(R_pos, B_pos, 0)
print(answer if answer != float('inf') else -1)
