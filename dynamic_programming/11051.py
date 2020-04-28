from sys import stdin


N, K = tuple(map(int, stdin.readline().split()))

# D[i][j] : C_ij의 값 (i개에서 j개를 뽑는 경우의 수)
D = [[0 for _ in range(K + 2)] for _ in range(N + 1)]

D[1][0] = 1
D[1][1] = 1

for i in range(2, N + 1):
	for j in range(K + 1):
		if j == 0 or j == i:
			D[i][j] = 1
		else:
			D[i][j] = D[i - 1][j - 1] + D[i - 1][j]

print(D[N][K] % 10007)