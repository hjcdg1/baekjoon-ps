from sys import stdin


N = int(stdin.readline())

# D[i] : 길이가 i인 오르막 수의 개수
D = [[0 for _ in range(10)] for _ in range(N + 1)]

for j in range(10):
	D[1][j] = 1

for i in range(2, N + 1):
	for j in range(10):
		for k in range(j + 1):
			D[i][j] += D[i - 1][k]
		D[i][j] = D[i][j] % 10007

print(sum(D[N]) % 10007)
