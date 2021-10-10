from sys import stdin
from copy import deepcopy
from itertools import combinations


N, M = list(map(int, stdin.readline().split()))
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

def spread_virus(A_temp, i, j):
	A_temp[i][j] = 2

	if i > 0 and A_temp[i - 1][j] == 0:
		spread_virus(A_temp, i - 1, j)
	if i < N - 1 and A_temp[i + 1][j] == 0:
		spread_virus(A_temp, i + 1, j)
	if j > 0 and A_temp[i][j - 1] == 0:
		spread_virus(A_temp, i, j - 1)
	if j < M - 1 and A_temp[i][j + 1] == 0:
		spread_virus(A_temp, i, j + 1)

empty_cells = []
virus_cells = []
for i in range(N):
	for j in range(M):
		if A[i][j] == 0:
			empty_cells.append((i, j))
		elif A[i][j] == 2:
			virus_cells.append((i, j))

answer = 0

for combination in combinations(empty_cells, 3):
	A_temp = deepcopy(A)

	# 벽 3개 세우기
	for i, j in combination:
		A_temp[i][j] = 1

	# 바이러스 퍼뜨려 보기
	for i, j in virus_cells:
		spread_virus(A_temp, i, j)

	# 빈 칸 개수 세기
	cnt = 0
	for i in range(N):
		for j in range(M):
			if A_temp[i][j] == 0:
				cnt += 1

	answer = max(answer, cnt)

print(answer)
