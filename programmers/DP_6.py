def solution(money):
	M = len(money)
	D = [[0, 0] for _ in range(M)]

	D[M - 1][0] = money[M - 1]
	D[M - 1][1] = 0

	D[M - 2][0] = max(money[M - 2], money[M - 1])
	D[M - 2][1] = money[M - 2]

	for i in reversed(range(1, M - 2)):
		D[i][0] = max(money[i] + D[i + 2][0], D[i + 1][0])
		D[i][1] = max(money[i] + D[i + 2][1], D[i + 1][1])

	D[0][0] = D[1][0]
	D[0][1] = money[0] + D[2][1]

	return max(D[0][0], D[0][1])