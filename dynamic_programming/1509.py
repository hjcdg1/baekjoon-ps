from sys import stdin


S = [0] + list(stdin.readline().rstrip())
N = len(S) - 1

# P[i][j] : S[i] ~ S[j] 팰린드롬 여부
P = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	P[i][i] = True

for i in range(1, N):
	P[i][i + 1] = True if S[i] == S[i + 1] else False

for d in range(2, N):
	for i in range(1, N - d + 1):
		start = i
		end = i + d
		if P[start + 1][end - 1] == True and S[start] == S[end]:
			P[start][end] = True
		else:
			P[start][end] = False

# D[i] : S[1] ~ S[i] 분할 개수의 최솟값
D = [0 for _ in range(N + 1)]

D[1] = 1
D[2] = 1 if S[1] == S[2] else 2

for i in range(3, N + 1):
	if P[1][i]:
		D[i] = 1
	else:
		D[i] = D[i - 1] + 1
		for j in range(2, i):
			if P[j][i]:
				D[i] = min(D[i], D[j - 1] + 1)

print(D[N])

"""
<Failed Solution : 시간 초과>

from sys import stdin


S = [0] + list(stdin.readline().rstrip())
N = len(S) - 1

# D[i][j] : S[i:j + 1] 분할 개수의 최솟값
D = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	D[i][i] = 1

for i in range(1, N):
	D[i][i + 1] = 1 if S[i] == S[i + 1] else 2

for d in range(2, N):
	for i in range(1, N - d + 1):
		start = i
		end = i + d
		if D[start + 1][end - 1] == 1 and S[start] == S[end]:
			D[start][end] = 1
		else:
			D[start][end] = float('inf')
			for k in range(start, end):
				D[start][end] = min(D[start][end], D[start][k] + D[k + 1][end])

print(D[1][N])
"""
