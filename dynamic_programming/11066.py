from sys import stdin

T = int(stdin.readline())
for _ in range(T):
	K = int(stdin.readline())
	S = [-1] + list(map(int, stdin.readline().split()))

	# D[i][j] : S[i] ~ S[j]를 합치는 최소 비용
	D = [[0 for _ in range(K + 1)] for _ in range(K + 1)]

	# A[i][j] : S[i] ~ S[j] 크기 합
	A = [[0 for _ in range(K + 1)] for _ in range(K + 1)]

	for i in range(1, K + 1):
		A[i][i], D[i][i] = S[i], 0

	for d in range(1, K):
		for i in range(1, K - d + 1):
			s, e = i, i + d

			A[s][e] = A[s][e - 1] + A[e][e]
			
			min_D = float('inf')
			for k in range(s, e):
				min_D = min(min_D, D[s][k] + D[k + 1][e] + A[s][e])
			D[s][e] = min_D

	print(D[1][K])