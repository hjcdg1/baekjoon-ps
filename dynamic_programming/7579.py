from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [0] + list(map(int, stdin.readline().split()))
C = [0] + list(map(int, stdin.readline().split()))

C_sum = sum(C[1:])

# D[i][j] : i번째 앱까지 고려할 때, 최대 j만큼의 비용으로 확보할 수 있는 최대 메모리 크기
D = [[0 for _ in range(C_sum + 1)] for _ in range(N + 1)]

for j in range(C_sum + 1):
	D[1][j] = A[1] if C[1] <= j else 0

for i in range(2, N + 1):
	for j in range(C_sum + 1):
		D[i][j] = D[i - 1][j]  # A[i] 미선택
		if C[i] <= j:
			D[i][j] = max(D[i][j], A[i] + D[i - 1][j - C[i]])  # A[i] 선택

for j in range(C_sum + 1):
	if D[N][j] >= M:
		print(j)
		break

"""
<Failed Solution 1 : 시간 초과>

from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [0] + list(map(int, stdin.readline().split()))
C = [0] + list(map(int, stdin.readline().split()))

# D[i][j] : i번째 앱까지 고려할 때, j만큼의 메모리를 확보하기 위해 필요한 최소의 비용
# D[0][j], D[1][j]로 최적화 (슬라이딩 윈도우 : 메모리 절약)
D = [[0 for _ in range(M + 1)] for _ in range(2)]

for j in range(1, M + 1):
	D[0][j] = float('inf')

old_idx = 0
new_idx = 1

for i in range(1, N + 1):
	for j in range(1, M + 1):
		if A[i] < j:
			D[new_idx][j] = min(C[i] + D[old_idx][j - A[i]], D[old_idx][j])
		else:
			D[new_idx][j] = min(C[i], D[old_idx][j])

	old_idx, new_idx = new_idx, old_idx

print(D[old_idx][M])
"""

"""
<Failed Solution 2 : 시간 초과>

from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [0] + list(map(int, stdin.readline().split()))
C = [0] + list(map(int, stdin.readline().split()))

# D[i][j] : i번째 앱부터 고려할 때, j만큼의 메모리를 확보하기 위해 필요한 최소의 비용
# D[0][j], D[1][j]로 최적화 (슬라이딩 윈도우 : 메모리 절약)
D = [[0 for _ in range(M + 1)] for _ in range(2)]

for j in range(M + 1):
	D[0][j] = C[N] if 0 < j <= A[N] else float('inf') if j > A[N] else 0

old_idx = 0
new_idx = 1

for i in reversed(range(1, N)):
	for j in range(M + 1):
		D[new_idx][j] = min(C[i] + D[old_idx][max(j - A[i], 0)], D[old_idx][j])

	old_idx, new_idx = new_idx, old_idx

print(D[old_idx][M])
"""
