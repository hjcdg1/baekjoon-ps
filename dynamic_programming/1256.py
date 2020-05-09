# Try again

from sys import stdin


N, M, K = tuple(map(int, stdin.readline().split()))

# C[i][j] : C_ij의 값
C = [[0 for _ in range(N + M + 1)] for _ in range(N + M + 1)]

C[1][0] = 1
C[1][1] = 1

for i in range(2, N + M + 1):
	C[i][0] = 1
	C[i][i] = 1
	for j in range(1, i):
		C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

if K > C[N + M][N]:
	print(-1)

else:
	result = []
	a, z = N, M
	for _ in range(N + M):
		if a == 0:
			result.append('z')
		elif z == 0:
			result.append('a')
		else:
			if K <= C[(a - 1) + z][z]:
				result.append('a')
				a -= 1
			else:
				result.append('z')
				K -= C[(a - 1) + z][z]
				z -= 1
	print(''.join(result))