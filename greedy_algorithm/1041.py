from sys import stdin


N = int(stdin.readline())
D = list(map(int, stdin.readline().split()))

# 한 면의 숫자 최솟값
min_1 = min(D)

# 인접한 두 면의 숫자 합 최솟값
min_2 = min([
	D[a] + D[b]
	for a, b in [(0, 1), (0, 3), (0, 4), (0, 2), (5, 1), (5, 3), (5, 4), (5, 2), (2, 1), (1, 3), (3, 4), (4, 2)]
])

# 인접한 세 면의 숫자 합 최솟값
min_3 = min([
	D[a] + D[b] + D[c] 
	for a, b, c in [(0, 2, 1), (0, 1, 3), (0, 3, 4), (0, 4, 2), (5, 2, 1), (5, 1, 3), (5, 3, 4), (5, 4, 2)]
])

if N == 1:
	print(sum(D) - max(D))
else:
	print(
		min_1 * (5 * (N - 2) ** 2 + 4 * (N - 2)) +
		min_2 * (8 * (N - 2) + 4) +
		min_3 * 4
	)
