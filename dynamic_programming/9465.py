from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N = int(stdin.readline())
	P = [[None] + list(map(int, stdin.readline().split())) for _ in range(2)]

	# D[i] : i번째 열까지 고려했을 때의 답
	D = [[-1, -1, -1] for _ in range(N + 1)]

	D[1][0] = P[0][1]
	D[1][1] = P[1][1]
	D[1][2] = 0

	for i in range(2, N + 1):
		D[i][0] = max(D[i - 1][1], D[i - 1][2]) + P[0][i]
		D[i][1] = max(D[i - 1][0], D[i - 1][2]) + P[1][i]
		D[i][2] = max(D[i - 1][0], D[i - 1][1])

	print(max(D[N]))