from sys import stdin


N = int(stdin.readline())
P = [None] + list(map(int, stdin.readline().split()))

# D[i] : 카드 i개를 갖기 위해 지불해야 하는 금액의 최댓값
D = [-1] * (N + 1)

D[1] = P[1]

for i in range(2, N + 1):
	max_D = P[i]
	for j in range(1, i):
		max_D = max(max_D, D[i - j] + P[j])
	D[i] = max_D

print(D[N])