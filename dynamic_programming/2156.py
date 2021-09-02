from sys import stdin


N = int(stdin.readline())
A = [None] + [int(stdin.readline()) for _ in range(N)]

# D[i][0] : (i - 1)번째 포도주를 마시고 i번째 포도주를 마셨을 때 마실 수 있는 총 양
# D[i][1] : (i - 1)번째 포도주를 마시지 않고 i번째 포도주를 마셨을 때 마실 수 있는 총 양
# D[i][2] : (i - 1)번째 포도주를 마시고 i번째 포도주를 마시지 않았을 때 마실 수 있는 총 양
# D[i][3] : (i - 1)번째 포도주를 마시지 않고 i번째 포도주를 마시지 않았을 때 마실 수 있는 총 양
D = [None] + [[0, 0, 0, 0] for _ in range(N)]

D[1][0] = A[1]
D[1][1] = A[1]
D[1][2] = 0
D[1][3] = 0

for i in range(2, N + 1):
	D[i][0] = A[i] + D[i - 1][1]
	D[i][1] = A[i] + max(D[i - 1][2], D[i - 1][3])
	D[i][2] = max(D[i - 1][0], D[i - 1][1])
	D[i][3] = max(D[i - 1][2], D[i - 1][3])

print(max(D[N]))
