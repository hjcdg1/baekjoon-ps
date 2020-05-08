from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N = int(stdin.readline())
	C = [-1] + list(map(int, stdin.readline().split()))
	M = int(stdin.readline())

	# D[i][j] : i번째 동전까지만 사용해서 j원을 만드는 경우의 수 (슬라이딩 윈도우 : 메모리 절약)
	D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

	for i in range(N + 1):
		D[i][0] = 1

	for i in range(1, N + 1):
		for j in range(1, M + 1):
			D[i][j] = D[i - 1][j]
			if C[i] <= j:
				D[i][j] += D[i][j - C[i]]

	print(D[N][M])