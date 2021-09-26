from sys import stdin
from itertools import product
from copy import deepcopy


def cover_scopes(A_copy, pos, scope):
	if 'R' in scope:
		for j in range(pos[1] + 1, M):
			if A_copy[pos[0]][j] == 6:
				break
			A_copy[pos[0]][j] = '#'

	if 'L' in scope:
		for j in reversed(range(0, pos[1])):
			if A_copy[pos[0]][j] == 6:
				break
			A_copy[pos[0]][j] = '#'

	if 'U' in scope:
		for i in reversed(range(0, pos[0])):
			if A_copy[i][pos[1]] == 6:
				break
			A_copy[i][pos[1]] = '#'

	if 'D' in scope:
		for i in range(pos[0] + 1, N):
			if A_copy[i][pos[1]] == 6:
				break
			A_copy[i][pos[1]] = '#'

N, M = list(map(int, stdin.readline().split()))
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

cctv_cells = []
for i in range(N):
	for j in range(M):
		if A[i][j] == 1:
			cctv_cells.append({
				'pos': (i, j),
				'scopes': ('U', 'R', 'D', 'L')
			})
		elif A[i][j] == 2:
			cctv_cells.append({
				'pos': (i, j),
				'scopes': ('RL', 'UD')
			})
		elif A[i][j] == 3:
			cctv_cells.append({
				'pos': (i, j),
				'scopes': ('UR', 'RD', 'DL', 'UL')
			})
		elif A[i][j] == 4:
			cctv_cells.append({
				'pos': (i, j),
				'scopes': ('URL', 'URD', 'RDL', 'UDL')
			})
		elif A[i][j] == 5:
			cctv_cells.append({
				'pos': (i, j),
				'scopes': ('URDL',)
			})

answer = float('inf')
for permutation in product(*map(lambda cctv_cell: cctv_cell['scopes'], cctv_cells)):
	A_copy = deepcopy(A)

	for idx, scope in enumerate(permutation):
		cover_scopes(A_copy, cctv_cells[idx]['pos'], scope)

	cnt = 0
	for i in range(N):
		for j in range(M):
			if A_copy[i][j] == 0:
				cnt += 1
	answer = min(answer, cnt)

print(answer)
