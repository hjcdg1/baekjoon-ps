# Try again

from sys import stdin


N, M = tuple(map(int, stdin.readline().split()))
A = [-1] + list(map(int, stdin.readline().split()))
C = [-1] + list(map(int, stdin.readline().split()))

C_min = min(C[1:])
C_sum = sum(C[1:])

# D[i][j] : A[1] ~ A[i]까지 고려할 때, 최대 j만큼의 비용으로 확보할 수 있는 최대 메모리 크기
D = [[0 for _ in range(C_sum + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
	for j in range(C_min, C_sum + 1):
		D[i][j] = D[i - 1][j]  # A[i] 미선택
		if C[i] <= j:
			D[i][j] = max(D[i][j], A[i] + D[i - 1][j - C[i]])  # A[i] 선택

for j in range(C_min, C_sum + 1):
	if D[N][j] >= M:
		print(j)
		break

"""
<첫 번째 풀이 : 시간 초과>
# D[i][j] : A[1] ~ A[i]까지 고려할 때, 확보해야 하는 메모리 크기가 j인 경우 (슬라이딩 윈도우 : 메모리 절약)
D = [[0 for _ in range(M + 1)] for _ in range(2)]

for j in range(1, M + 1):
	D[0][j] = float('inf')

old_is_0 = True
for i in range(1, N + 1):
	old_D = D[0] if old_is_0 else D[1]
	new_D = D[1] if old_is_0 else D[0]
	for j in range(1, M + 1):
		if A[i] < j:
			new_D[j] = min(C[i] + old_D[j - A[i]], old_D[j])
		else:
			new_D[j] = min(C[i], old_D[j])
	old_is_0 = not old_is_0

old_D = D[0] if old_is_0 else D[1]
print(old_D[M])
"""