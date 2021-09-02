from sys import stdin


N = int(stdin.readline())
S = [None] + list(map(int, stdin.readline().split()))

# D[i][0] : i번째 수까지 고려했을 때, 끝 수를 포함하는 답
# D[i][1] : i번째 수까지 고려했을 때, 끝 수를 포함하지 않는 답
D = [None] + [[0, 0] for _ in range(N)]

D[1][0] = S[1]
D[1][1] = -1001

for i in range(2, N + 1):
	D[i][0] = max(S[i], D[i - 1][0] + S[i])
	D[i][1] = max(D[i - 1])

print(max(D[N]))
