from sys import stdin


N, K = list(map(int, stdin.readline().split()))

# C[i][j] : i개에서 순서 상관 없이 j개를 뽑는 경우의 수
C = [[0 for _ in range(i + 1)] for i in range(N + 1)]

C[1][0] = 1
C[1][1] = 1

for i in range(2, N + 1):
	for j in range(i + 1):
		if j == 0 or j == i:
			C[i][j] = 1
		else:
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % 10007

print(C[N][K])
