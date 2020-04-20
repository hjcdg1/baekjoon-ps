from sys import stdin


N = int(stdin.readline())
D = list(map(int, stdin.readline().split()))

# 인접한 세 면의 숫자 합 최솟값
C_3 = [(0, 2, 1), (0, 1, 3), (0, 3, 4), (0, 4, 2), (5, 2, 1), (5, 1, 3), (5, 3, 4), (5, 4, 2)]
min_3 = None
for c in C_3:
	if min_3 is None:
		min_3 = sum([D[c[0]], D[c[1]], D[c[2]]])
	else:
		min_3 = min(min_3, sum([D[c[0]], D[c[1]], D[c[2]]]))

# 인접한 두 면의 숫자 합 최솟값
C_2 = [(0, 1), (0, 3), (0, 4), (0, 2), (5, 1), (5, 3), (5, 4), (5, 2), (2, 1), (1, 3), (3, 4), (4, 2)]
min_2 = None
for c in C_2:
	if min_2 is None:
		min_2 = sum([D[c[0]], D[c[1]]])
	else:
		min_2 = min(min_2, sum([D[c[0]], D[c[1]]]))

# 한 면의 숫자 최솟값
min_1 = min(D)

if N == 1:
	print(sum(D) - max(D))
else:
	top_area = min_1 * (N - 2) * (N - 2) * 1
	top_edge = min_2 * (N - 2) * 4
	top_point = min_3 * 4
	side_area = min_1 * (N - 2) * (N - 1) * 4
	side_edge = min_2 * (N - 1) * 4
	print(top_area + top_edge + top_point + side_area + side_edge)