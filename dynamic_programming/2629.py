from sys import stdin


N = int(stdin.readline())
W = [0] + list(map(int, stdin.readline().split()))
T = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

W_sum = sum(W[1:])

# D[i][j] : i번째 추까지 사용할 때 j만큼의 무게를 확인할 수 있는지 여부
D = [[False for _ in range(W_sum + 1)] for _ in range(N + 1)]

D[1][W[1]] = True

for i in range(2, N + 1):
	for j in range(1, W_sum + 1):
		if j == W[i]:
			D[i][j] = True
		else:
			D[i][j] = D[i - 1][j] or D[i - 1][abs(j - W[i])]
			if j + W[i] <= W_sum:
				D[i][j] = D[i][j] or D[i - 1][j + W[i]]

print(' '.join(['Y' if a <= W_sum and D[N][a] else 'N' for a in A]))
