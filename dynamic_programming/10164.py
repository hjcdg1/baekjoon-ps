# Try again

from sys import stdin


N, M, K = tuple(map(int, stdin.readline().split()))
min_NM = min(N, M)

# C[i][j] : i개에서 순서 없이 j를 선택하는 경우의 수
C = [[0 for _ in range(N + M - 1)] for _ in range(N + M - 1)]

C[1][0] = 1
C[1][1] = 1

for i in range(2, N + M - 1):
	C[i][0] = 1
	C[i][i] = 1
	for j in range(1, i):
		C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

if K == 0:
	print(C[N + M - 2][N - 1])
else:
	if K % M == 0:
		K_i, K_j = K // M, M
	else:
		K_i, K_j = K // M + 1, K % M
	print(C[K_i + K_j - 2][K_i - 1] * C[N - K_i + M - K_j][N - K_i])