from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N = int(stdin.readline())
	C = [0] + list(map(int, stdin.readline().split()))
	M = int(stdin.readline())

	# D[i][j] : i번째 동전까지만 사용해서 j원을 만드는 경우의 수
	# D[j]로 최적화 (슬라이딩 윈도우 : 메모리 절약)
	D = [0 for _ in range(M + 1)]

	D[0] = 1

	for i in range(1, N + 1):
		for j in range(M + 1):
			if j - C[i] >= 0:
				D[j] += D[j - C[i]]

	print(D[M])
