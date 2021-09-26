from sys import stdin


def is_ok(A, x_pos, y_pos, direction):
	"""
	x_pos 위치의 공을 direction 방향으로 움직일 수 있는지 여부를 반환한다.
	y_pos 위치에는 다른 색의 공이 위치하고 있다.

	1. 움직이려는 위치에 구멍이 있으면 이동 가능 (다른 색의 공이 앞에 있었어도 구멍에 빠졌을 것)
	2. 움직이려는 위치에 벽 혹은 다른 색의 공이 없으면 이동 가능
	"""

	x_i, x_j = x_pos
	y_i, y_j = y_pos

	if direction == 'L':
		if A[x_i][x_j - 1] == 'O':
			return True
		else:
			return A[x_i][x_j - 1] != '#' and (x_i, x_j - 1) != (y_i, y_j)
	elif direction == 'R':
		if A[x_i][x_j + 1] == 'O':
			return True
		else:
			return A[x_i][x_j + 1] != '#' and (x_i, x_j + 1) != (y_i, y_j)
	elif direction == 'U':
		if A[x_i - 1][x_j ] == 'O':
			return True
		else:
			return A[x_i - 1][x_j] != '#' and (x_i - 1, x_j) != (y_i, y_j)
	else:
		if A[x_i + 1][x_j ] == 'O':
			return True
		else:
			return A[x_i + 1][x_j] != '#' and (x_i + 1, x_j) != (y_i, y_j)

def dfs(A, r_pos, b_pos, cnt):
	# 이미 10번 이상 움직였으면 더 이상 움직일 수 없음
	if cnt == 10:
		return float('inf')

	# 왼쪽으로 움직이는 경우
	status = None
	r_i, r_j = r_pos
	b_i, b_j = b_pos
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'L'):
		r_j -= 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	while is_ok(A, (b_i, b_j), (r_i, r_j), 'L'):
		b_j -= 1
		if A[b_i][b_j] == 'O':
			status = 'failure'
			break
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'L') and status is None:
		r_j -= 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	if (r_i, r_j) == r_pos and (b_i, b_j) == b_pos:
		status = 'failure'
	if status == 'success':
		when_left = cnt + 1
	elif status == 'failure':
		when_left = float('inf')
	else:
		when_left = dfs(A, (r_i, r_j), (b_i, b_j), cnt + 1)

	# 오른쪽으로 움직이는 경우
	status = None
	r_i, r_j = r_pos
	b_i, b_j = b_pos
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'R'):
		r_j += 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	while is_ok(A, (b_i, b_j), (r_i, r_j), 'R'):
		b_j += 1
		if A[b_i][b_j] == 'O':
			status = 'failure'
			break
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'R') and status is None:
		r_j += 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	if (r_i, r_j) == r_pos and (b_i, b_j) == b_pos:
		status = 'failure'
	if status == 'success':
		when_right = cnt + 1
	elif status == 'failure':
		when_right = float('inf')
	else:
		when_right = dfs(A, (r_i, r_j), (b_i, b_j), cnt + 1)

	# 위쪽으로 움직이는 경우
	status = None
	r_i, r_j = r_pos
	b_i, b_j = b_pos
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'U'):
		r_i -= 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	while is_ok(A, (b_i, b_j), (r_i, r_j), 'U'):
		b_i -= 1
		if A[b_i][b_j] == 'O':
			status = 'failure'
			break
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'U') and status is None:
		r_i -= 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	if (r_i, r_j) == r_pos and (b_i, b_j) == b_pos:
		status = 'failure'
	if status == 'success':
		when_up = cnt + 1
	elif status == 'failure':
		when_up = float('inf')
	else:
		when_up = dfs(A, (r_i, r_j), (b_i, b_j), cnt + 1)

	# 아래쪽으로 움직이는 경우
	status = None
	r_i, r_j = r_pos
	b_i, b_j = b_pos
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'D'):
		r_i += 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	while is_ok(A, (b_i, b_j), (r_i, r_j), 'D'):
		b_i += 1
		if A[b_i][b_j] == 'O':
			status = 'failure'
			break
	while is_ok(A, (r_i, r_j), (b_i, b_j), 'D') and status is None:
		r_i += 1
		if A[r_i][r_j] == 'O':
			status = 'success'
			break
	if (r_i, r_j) == r_pos and (b_i, b_j) == b_pos:
		status = 'failure'
	if status == 'success':
		when_down = cnt + 1
	elif status == 'failure':
		when_down = float('inf')
	else:
		when_down = dfs(A, (r_i, r_j), (b_i, b_j), cnt + 1)

	return min(when_left, when_right, when_up, when_down)

N, M = list(map(int, stdin.readline().split()))
A = [list(stdin.readline().rstrip()) for _ in range(N)]

# 빨간 공과 파란 공의 위치
R_pos, B_pos = None, None
for i in range(N):
	for j in range(M):
		if A[i][j] == 'R':
			R_pos = (i, j)
		elif A[i][j] == 'B':
			B_pos = (i, j)

answer = dfs(A, R_pos, B_pos, 0)
print(answer if answer != float('inf') else -1)
