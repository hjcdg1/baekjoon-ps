from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [0] + [[0] + list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]

# D[i][j] : A[i][j]가 마지막 수인 정사각형 중 가장 큰 정사각형의 한 변 길이 
D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	for j in range(1, M + 1):
		if A[i][j] == 0:
			continue

		if i == 1 or j == 1:
			D[i][j] = 1
		else:
			L = D[i][j - 1]
			R = D[i - 1][j]
			if L == R and D[i - 1][j - 1] < L:
				D[i][j] = L
			else:
				D[i][j] = min(L + 1, R + 1)

print(max([max(d[1:]) for d in D[1:]]) ** 2)
