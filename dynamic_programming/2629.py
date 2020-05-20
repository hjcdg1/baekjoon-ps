# Try again

from sys import stdin


N = int(stdin.readline())
W = [0] + list(map(int, stdin.readline().split()))
T = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

W_sum = sum(W[1:])

# D[i][j] : 1 ~ i번째 추가 있을 때, 무게 차이 j를 평형으로 만들 수 있는가?
D = [[False for _ in range(W_sum + 1)] for _ in range(N + 1)]

for i in range(N + 1):
	D[i][0] = True

for i in range(1, N + 1):
	for j in range(1, W_sum + 1):
		D[i][j] = D[i - 1][j] or D[i - 1][abs(j - W[i])]
		if j + W[i] <= W_sum:
			D[i][j] = D[i][j] or D[i - 1][j + W[i]]

for t in range(T):
	if A[t] > W_sum:
		print('N', end=" ")
	else:
		print('Y' if D[N][A[t]] else 'N', end=" ")