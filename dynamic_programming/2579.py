from sys import stdin


N = int(stdin.readline())
P = [0] + [int(stdin.readline()) for _ in range(N)]

if N == 1:
	print(P[1])

else:
	# D[i][0] : (i - 1)번째 계단을 거쳐서 i번째 계단까지 올라올 때 얻을 수 있는 최대 점수
	# D[i][1] : (i - 1)번째 계단을 거치지 않고 i번째 계단까지 올라올 때 얻을 수 있는 최대 점수
	D = [[0, 0] for _ in range(N + 1)]

	D[1][0] = P[1]
	D[1][1] = P[1]
	D[2][0] = P[1] + P[2]
	D[2][1] = P[2]

	for i in range(3, N + 1): 
		D[i][0] = D[i - 1][1] + P[i]
		D[i][1] = max(D[i - 2][0], D[i - 2][1]) + P[i]

	print(max(D[N]))
