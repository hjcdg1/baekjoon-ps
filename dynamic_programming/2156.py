from sys import stdin


N = int(stdin.readline())
A = [-1] + [int(stdin.readline()) for _ in range(N)]

if N == 1:
	print(A[1])
elif N == 2:
	print(A[1] + A[2])
else:
	# D[i][0] : (i - 1)번째 포도주를 마시고 i번째 포도주까지 마셨을 때 마실 수 있는 총 양
	# D[i][1] : (i - 1)번째 포도주를 마시지 않고 i번째 포도주까지 마셨을 때 마실 수 있는 총 양
	D = [None] * (N + 2)

	D[1] = [A[1], A[1], 0, 0]
	D[2] = [A[1] + A[2], A[2], A[1], 0]

	for i in range(3, N + 1):
		D[i] = [-1, -1, -1, -1]
		D[i][0] = D[i - 1][1] + A[i]
		D[i][1] = max(D[i - 1][2], D[i - 1][3]) + A[i]
		D[i][2] = max(D[i - 1][0], D[i - 1][1])
		D[i][3] = max(D[i - 1][2], D[i - 1][3])

	print(max(D[N]))