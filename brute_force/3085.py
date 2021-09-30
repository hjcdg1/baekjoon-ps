from sys import stdin
from itertools import product


def get_sequence_max_length(A):
	candidates = []

	# 각 행별로 가장 긴 연속 줄의 길이 찾기
	for i in range(N):
		prev_color = A[i][0]
		curr_length = 1
		max_length = 1

		for j in range(1, N):
			if A[i][j] == prev_color:
				curr_length += 1
				if curr_length > max_length:
					max_length = curr_length
			else:
				prev_color = A[i][j]
				curr_length = 1
		candidates.append(max_length)

	# 각 열별로 가장 긴 줄의 길이 찾기
	for j in range(N):
		prev_color = A[0][j]
		curr_length = 1
		max_length = 1

		for i in range(1, N):
			if A[i][j] == prev_color:
				curr_length += 1
				if curr_length > max_length:
					max_length = curr_length
			else:
				prev_color = A[i][j]
				curr_length = 1
		candidates.append(max_length)

	return max(candidates)

N = int(stdin.readline())
A = [list(stdin.readline().rstrip()) for _ in range(N)]

candidates = [get_sequence_max_length(A)]

for i, j in product(range(N), repeat=2):
	# 오른쪽 칸의 사탕과 교환
	if j < N - 1 and A[i][j] != A[i][j + 1]:
		A[i][j], A[i][j + 1] = A[i][j + 1], A[i][j]
		candidates.append(get_sequence_max_length(A))
		A[i][j], A[i][j + 1] = A[i][j + 1], A[i][j]

	# 아래쪽 칸의 사탕과 교환
	if i < N - 1 and A[i][j] != A[i + 1][j]:
		A[i][j], A[i + 1][j] = A[i + 1][j], A[i][j]
		candidates.append(get_sequence_max_length(A))
		A[i][j], A[i + 1][j] = A[i + 1][j], A[i][j]

print(max(candidates))
