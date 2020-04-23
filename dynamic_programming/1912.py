from sys import stdin


N = int(stdin.readline())
S = [None] + list(map(int, stdin.readline().split()))

if N == 1:
	print(S[1])
else:
	# D[i][0] : i번째 수까지 고려했을 때, 끝 수를 포함하는 답
	# D[i][1] : i번째 수까지 고려했을 때, 끝 수를 포함하지 않는 답
	D = [[-1, -1] for _ in range(N + 1)]

	D[1] = [S[1], -1001]
	D[2] = [S[1] + S[2] if S[1] > 0 else S[2], S[1]]

	for i in range(3, N + 1):
		D[i][0] = max(S[i], D[i - 1][0] + S[i])
		D[i][1] = max(D[i - 1][0], D[i - 1][1])

	print(max(D[N][0], D[N][1]))