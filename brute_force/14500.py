from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = float('-inf')

for i in range(N - 3):
	for j in range(M - 3):
		# 첫 번째 테트로미노
		for p in range(i, i + 4):
			answer = max(answer, A[p][j] + A[p][j + 1] + A[p][j + 2] + A[p][j + 3])
		for q in range(j, j + 4):
			answer = max(answer, A[i][q] + A[i + 1][q] + A[i + 2][q] + A[i + 3][q])

		# 두 번째 테트로미노
		for p in range(i, i + 3):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q] + A[p + 1][q] + A[p][q + 1] + A[p + 1][q + 1])

		# 세 번째 테트로미노
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q] + A[p + 1][q] + A[p + 2][q] + A[p + 2][q + 1])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q] + A[p][q + 1] + A[p][q + 2] + A[p + 1][q])
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q] + A[p][q + 1] + A[p + 1][q + 1] + A[p + 2][q + 1])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q + 2] + A[p + 1][q + 2] + A[p + 1][q + 1] + A[p + 1][q])
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q + 1] + A[p + 1][q + 1] + A[p + 2][q + 1] + A[p + 2][q])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q] + A[p + 1][q] + A[p + 1][q + 1] + A[p + 1][q + 2])
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q] + A[p][q + 1] + A[p + 1][q] + A[p + 2][q])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q] + A[p][q + 1] + A[p][q + 2] + A[p + 1][q + 2])

		# 네 번째 테트로미노
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q] + A[p + 1][q] + A[p + 1][q + 1] + A[p + 2][q + 1])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q + 1] + A[p][q + 2] + A[p + 1][q + 1] + A[p + 1][q])
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q + 1] + A[p + 1][q + 1] + A[p + 1][q] + A[p + 2][q])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q] + A[p][q + 1] + A[p + 1][q + 1] + A[p + 1][q + 2])

		# 다섯 번째 테트로미노
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p][q] + A[p][q + 1] + A[p][q + 2] + A[p + 1][q + 1])
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q + 1] + A[p + 1][q + 1] + A[p + 1][q] + A[p + 2][q + 1])
		for p in range(i, i + 3):
			for q in range(j, j + 2):
				answer = max(answer, A[p + 1][q] + A[p + 1][q + 1] + A[p + 1][q + 2] + A[p][q + 1])
		for p in range(i, i + 2):
			for q in range(j, j + 3):
				answer = max(answer, A[p][q] + A[p + 1][q] + A[p + 2][q] + A[p + 1][q + 1])

print(answer)
