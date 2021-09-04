from sys import stdin


N = int(stdin.readline())

# D[i] : 길이가 i인 모든 2진 수열의 개수
D = [None] + [0 for _ in range(N + 1)]

D[1] = 1
D[2] = 2

for i in range(3, N + 1):
	D[i] = (D[i - 1] + D[i - 2]) % 15746

print(D[N])
