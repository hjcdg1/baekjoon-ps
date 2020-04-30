from sys import stdin


N, K = tuple(map(int, stdin.readline().split()))

# D[i][j] : 0부터 i까지의 정수 j개를 사용하여 i를 만드는 경우의 수
D = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for j in range(K + 1):
	D[0][j] = 1

for i in range(1, N + 1):
	for j in range(1, K + 1):
		for k in range(i + 1):
			D[i][j] += D[i - k][j - 1]

print(D[N][K] % 1000000000)