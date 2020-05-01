from sys import stdin


N = int(stdin.readline())
A = [-1] + list(map(int, stdin.readline().split()))

# D[i][j] : A[i]까지의 결과가 j인 경우의 수
D = [[0 for _ in range(21)] for _ in range(N)]

D[1][A[1]] = 1

for i in range(2, N):
	for j in range(21):
		if A[i] == 0:
			D[i][j] = 2 * D[i - 1][j]
		else:
			D[i][j] = 0
			if 0 <= j - A[i] <= 20:  # + A[i]
				D[i][j] += D[i - 1][j - A[i]]
			if 0 <= j + A[i] <= 20:  # - A[i]
				D[i][j] += D[i - 1][j + A[i]]

print(D[N - 1][A[-1]])