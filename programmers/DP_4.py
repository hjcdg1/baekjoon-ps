def solution(m, n, puddles):
	D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

	D[n][m] = 1
	for puddle in puddles:
		D[puddle[1]][puddle[0]] = -1

	for i in reversed(range(1, n + 1)):
		for j in reversed(range(1, m + 1)):
			if D[i][j] != -1:
				if i + 1 <= n:
					D[i][j] += D[i + 1][j]
				if j + 1 <= m:
					D[i][j] += D[i][j + 1]
				D[i][j] %= 1000000007
			else:
				D[i][j] = 0

	return D[1][1]