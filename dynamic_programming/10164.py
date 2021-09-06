from sys import stdin
import math


N, M, K = list(map(int, stdin.readline().split()))

min_NM = min(N, M)

# C[i][j] : i개에서 순서 상관 없이 j개를 뽑는 경우의 수
C = [[0 for _ in range(N + M - 1)] for _ in range(N + M - 1)]

C[1][0] = 1
C[1][1] = 1

for i in range(2, N + M - 1):
	for j in range(i + 1):
		if j == 0 or j == i:
			C[i][j] = 1
		else:
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

if K == 0:
	print(C[N + M - 2][N - 1])
else:
	K_N = math.ceil(K / M)
	K_M = K % M if K % M > 0 else M

	print(C[K_N + K_M - 2][K_N - 1] * C[N + M - K_N - K_M][N - K_N])
