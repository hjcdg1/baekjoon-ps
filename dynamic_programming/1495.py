from sys import stdin


N, S, M = list(map(int, stdin.readline().split()))
V = [0] + list(map(int, stdin.readline().split()))

# D[i][j] : i번 곡 연주 직전의 볼륨이 j일 때의 답
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for j in range(M + 1):
	if j + V[N] <= M:
		D[N][j] = j + V[N]
	elif j - V[N] >= 0:
		D[N][j] = j - V[N]
	else:
		D[N][j] = -1

for i in reversed(range(1, N)):
	for j in range(M + 1):
		D[i][j] = -1
		if j + V[i] <= M:
			D[i][j] = max(D[i][j], D[i + 1][j + V[i]])
		if j - V[i] >= 0:
			D[i][j] = max(D[i][j], D[i + 1][j - V[i]])

print(D[1][S])
