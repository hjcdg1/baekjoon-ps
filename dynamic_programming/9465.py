from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N = int(stdin.readline())
	P = [[None] + list(map(int, stdin.readline().split())) for _ in range(2)]

	# D[i][0] : i번째 열까지 고려했을 때, i번째 열에서 첫 번째 행의 스티커를 선택한 경우
	# D[i][1] : i번째 열까지 고려했을 때, i번째 열에서 두 번째 행의 스티커를 선택한 경우
	# D[i][2] : i번째 열까지 고려했을 때, i번째 열에서 스티커를 선택하지 않은 경우
	D = [None] + [[0, 0, 0] for _ in range(N)]

	D[1][0] = P[0][1]
	D[1][1] = P[1][1]
	D[1][2] = 0

	for i in range(2, N + 1):
		D[i][0] = max(D[i - 1][1], D[i - 1][2]) + P[0][i]
		D[i][1] = max(D[i - 1][0], D[i - 1][2]) + P[1][i]
		D[i][2] = max(D[i - 1][0], D[i - 1][1])

	print(max(D[N]))
