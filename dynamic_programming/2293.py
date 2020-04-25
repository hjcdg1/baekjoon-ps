# Try again

from sys import stdin


N, K = tuple(map(int, stdin.readline().split()))
C = [-1] + [int(stdin.readline()) for _ in range(N)]
C.sort()

# D[i][j] : 최대 i번째 동전까지만 사용하여 j원을 만드는 경우의 수 (슬라이딩 윈도우 : 메모리 절약)
D = [1] + [0 for _ in range(K)]

for i in range(1, N + 1):
	for j in range(1, K + 1):
		if C[i] <= j:
			D[j] = D[j] + D[j - C[i]]

print(D[K])

"""
<O(NK) 메모리>

for i in range(1, N + 1):
	for j in range(1, K + 1):
		if C[i] > j:
			D[i][j] = D[i - 1][j]
		else:
			D[i][j] = D[i - 1][j] + D[i][j - C[i]]
"""