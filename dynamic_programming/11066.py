from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	K = int(stdin.readline())
	C = [0] + list(map(int, stdin.readline().split()))

	# D[i][j] : S[i] ~ S[j]를 합치는 최소 비용
	D = [[0 for _ in range(K + 1)] for _ in range(K + 1)]

	# S[i][j] : S[i] ~ S[j] 크기 합
	S = [[0 for _ in range(K + 1)] for _ in range(K + 1)]

	for i in range(1, K + 1):
		S[i][i] = C[i]

	for d in range(1, K):
		for i in range(1, K - d + 1):
			start = i
			end = i + d

			S[start][end] = S[start][start] + S[start + 1][end]

			D[start][end] = float('inf')
			for k in range(start, end):
				D[start][end] = min(D[start][end], D[start][k] + D[k + 1][end] + S[start][end])

	print(D[1][K])
