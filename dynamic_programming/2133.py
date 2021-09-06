from sys import stdin


N = int(stdin.readline())

# D[i] : 3 x i 크기의 벽을 채우는 경우의 수
D = [0 for _ in range(N + 2)]

D[0] = 1
D[2] = 3

for i in range(3, N + 1):
	D[i] = 3 * D[i - 2]
	for j in range(4, i + 1, 2):
		D[i] += 2 * D[i - j]

print(D[N])
