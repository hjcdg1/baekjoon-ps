from sys import stdin


N = int(stdin.readline())
P = [-1] + [int(stdin.readline()) for _ in range(N)]

if N == 1:
	print(P[1])

else:
	# D[i][0] : (i - 1)번째 계단을 거쳐서 i번째 계단까지 올라올 때 얻을 수 있는 총 점수
	# D[i][1] : (i - 1)번째 계단을 거치지 않고 i번째 계단까지 올라올 때 얻을 수 있는 총 점수
	D = [None] * (N + 1)

	D[1] = (P[1], P[1])
	D[2] = (P[1] + P[2], P[2])

	for i in range(3, N + 1): 
		D[i] = (D[i - 1][1] + P[i], max(D[i - 2][0], D[i - 2][1]) + P[i])

	print(max(D[N][0], D[N][1]))