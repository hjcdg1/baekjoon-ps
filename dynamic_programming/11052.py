from sys import stdin


N = int(stdin.readline())
P = [0] + list(map(int, stdin.readline().split()))

# D[i] : 카드 i개를 갖기 위해 지불해야 하는 금액의 최댓값
D = [0 for _ in range(N + 1)]

D[1] = P[1]

for i in range(2, N + 1):
	D[i] = max([P[i]] + [P[j] + D[i - j] for j in range(1, i)])

print(D[N])
