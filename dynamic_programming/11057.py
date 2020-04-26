from sys import stdin


N = int(stdin.readline())

# D[i] : 길이가 i인 오르막 수의 개수
D = [None for _ in range(N + 1)]

D[1] = [1 for _ in range(10)]

for i in range(2, N + 1):
	D[i] = [0 for _ in range(10)]
	for j in range(10):
		for k in range(j + 1):
			D[i][j] += D[i - 1][k]

print(sum(D[N]))