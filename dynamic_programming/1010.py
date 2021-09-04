from sys import stdin


T = int(stdin.readline())
N, M = [], []
for _ in range(T):
	NM = list(map(int, stdin.readline().split()))
	N.append(NM[0])
	M.append(NM[1])

max_N, max_M = max(N), max(M)

# C[i][j] : i개에서 순서 상관 없이 j개를 뽑는 경우의 수
C = [None] + [[0 for _ in range(i + 2)] for i in range(max_M)]

C[1][0] = 1
C[1][1] = 1

for i in range(2, max_M + 1):
	for j in range(i + 1):
		if j == 0 or j == i:
			C[i][j] = 1
		else:
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

for t in range(T):
	print(C[M[t]][N[t]])
