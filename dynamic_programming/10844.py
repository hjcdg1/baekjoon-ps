from sys import stdin


N = int(stdin.readline())

# D[i][j] : 길이가 i인, 끝 수가 j인 계단 수의 개수
D = [[0 for _ in range(10)] for _ in range(N + 1)]

for j in range(1, 10):
	D[1][j] = 1

for i in range(2, N + 1):
	D[i][0] = D[i - 1][1] % 1000000000
	for j in range(1, 9):
		D[i][j] = (D[i - 1][j - 1] + D[i - 1][j + 1]) % 1000000000
	D[i][9] = D[i - 1][8] % 1000000000

print(sum(D[N]) % 1000000000)
