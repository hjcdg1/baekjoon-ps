from sys import stdin


T = int(stdin.readline())
N, M = [], []
for _ in range(T):
	NM = tuple(map(int, stdin.readline().split()))
	N.append(NM[0])
	M.append(NM[1])

max_N, max_M = max(N), max(M)

# D[i][j] : i x j 다리를 연결하는 경우의 수
D = [[-1 for _ in range(max_M + 1)] for _ in range(max_N + 1)]

for j in range(1, max_M + 1):
	D[1][j] = j

for i in range(2, max_N + 1):
	for j in range(1, max_M + 1):
		if i > j:
			D[i][j] = 0
		elif i == j:
			D[i][j] = 1
		else:
			D[i][j] = sum([D[i - 1][j - k] for k in range(1, j)])

for t in range(T):
	print(D[N[t]][M[t]])