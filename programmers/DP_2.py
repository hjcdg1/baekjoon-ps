def solution(N):
	D = [0 for _ in range(N + 1)]

	D[1] = 1
	D[2] = 1

	for i in range(3, N + 1):
		D[i] = D[i - 1] + D[i - 2]

	return D[N] * 2 + (D[N] + D[N - 1]) * 2