from sys import stdin


N, S, M = tuple(map(int, stdin.readline().split()))
V = [-1] + list(map(int, stdin.readline().split()))

# D[i][s] : i번 곡 연주 직전의 볼륨이 s일 때의 답
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for s in range(M + 1):
	if s + V[N] <= M:
		D[N][s] = s + V[N]
	elif s - V[N] >= 0:
		D[N][s] = s - V[N]
	else:
		D[N][s] = -1

for i in reversed(range(1, N)):
	for s in range(M + 1):
		max_D = -1
		if s + V[i] <= M:
			max_D = max(max_D, D[i + 1][s + V[i]])
		if s - V[i] >= 0:
			max_D = max(max_D, D[i + 1][s - V[i]])
		D[i][s] = max_D

print(D[1][S])