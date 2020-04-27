# Try again

from sys import stdin


N, K = tuple(map(int, stdin.readline().split()))
C = [None] + [int(stdin.readline()) for _ in range(N)]

# D[i] : i원을 만드는 동전의 최소 개수
D = [0 for _ in range(K + 1)]

for i in range(1, K + 1):
	min_D = 100001
	for j in range(1, N + 1):
		if i >= C[j] and D[i - C[j]] != -1:
			min_D = min(min_D, D[i - C[j]])
	D[i] = min_D + 1 if min_D != 100001 else -1

print(D[K])

"""
<어려운 풀이>

# D[i][j] : i번째 동전까지 사용하여 j원을 만드는 동전의 최소 개수
D = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for j in range(1, K + 1):
	D[0][j] = -1

for i in range(1, N + 1):
	for j in range(1, K + 1):
		if j >= C[i]:
			c1, c2 = D[i][j - C[i]], D[i - 1][j]
			if c1 == -1 and c2 == -1:
				D[i][j] = -1
			elif c1 == -1:
				D[i][j] = c2
			elif c2 == -1:
				D[i][j] = c1 + 1
			else:
				D[i][j] = min(c1 + 1, c2)
		else:
			D[i][j] = D[i - 1][j]

print(D[N][K])
"""