def solution(triangle):
	H = len(triangle)

	D = [[0 for _ in range(i + 1)] for i in range(H)]

	for j in range(H):
		D[H - 1][j] = triangle[H - 1][j]

	for i in reversed(range(H - 1)):
		for j in range(i + 1):
			D[i][j] = triangle[i][j] + max(D[i + 1][j], D[i + 1][j + 1])

	return D[0][0]