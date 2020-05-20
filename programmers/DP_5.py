def solution(left, right):
	L, R = len(left), len(right)

	D = [[0 for _ in range(R + 1)] for _ in range(L + 1)]

	for i in reversed(range(L)):
		for j in reversed(range(R)):
			D[i][j] = max(D[i + 1][j], D[i + 1][j + 1])
			if left[i] > right[j]:
				D[i][j] = max(D[i][j], D[i][j + 1] + right[j])

	return D[0][0]