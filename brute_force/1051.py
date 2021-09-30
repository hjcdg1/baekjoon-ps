from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [list(stdin.readline().rstrip()) for _ in range(N)]

max_side = min(N, M)
candidates = []

for i in range(N):
	for j in range(M):
		max_area = 1
		for side in range(2, min(N - i, M - j) + 1):
			if A[i][j] == A[i + side - 1][j] == A[i][j + side - 1] == A[i + side - 1][j + side - 1]:
				max_area = int(side) * int(side)
		candidates.append(max_area)

print(max(candidates))
