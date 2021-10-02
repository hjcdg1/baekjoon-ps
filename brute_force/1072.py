from sys import stdin


def get_min_cnt(start, end):
	if start == end:
		return start

	half = (start + end) // 2
	new_Z = ((Y + half) * 100) // (X + half)

	if new_Z >= Z + 1:
		return get_min_cnt(start, half)
	else:
		return get_min_cnt(half + 1, end)

X, Y = list(map(int, stdin.readline().split()))

Z = (Y * 100) // X

if Z >= 99:
	print(-1)

else:
	print(get_min_cnt(1, X))
