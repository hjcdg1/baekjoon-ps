from sys import stdin


N, M = tuple(map(int, stdin.readline().split()))
A = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]

# D[i][j] : A[i - 1][j - 1]가 마지막 수인 정사각형의 최대 너비
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

max_D = 0
for i in range(1, N + 1):
	for j in range(1, M + 1):
		if A[i - 1][j - 1] == 1:
			l_square = D[i][j - 1]
			r_sqaure = D[i - 1][j]

			if l_square == 0 or r_sqaure == 0:
				D[i][j] = 1
			else:
				if l_square == r_sqaure:
					D[i][j] = l_square if A[i - 1 - l_square][j - 1 - l_square] != 1 else l_square + 1
				elif l_square > r_sqaure:
					D[i][j] = r_sqaure + 1
				else:
					D[i][j] = l_square + 1
		else:
			D[i][j] = 0

		if D[i][j] > max_D:
			max_D = D[i][j]

print(max_D * max_D)