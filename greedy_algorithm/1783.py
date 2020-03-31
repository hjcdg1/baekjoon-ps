import sys


N, M = tuple(map(int, sys.stdin.readline().split()))

if N == 1:
	print(1)

elif N == 2:
	print(min((M - 1) // 2, 3) + 1)

elif N >= 3:
	if M >= 7:
		total_move_cnt = 2
		M = M - 4
		too_small = False
	else:
		total_move_cnt = 0
		too_small = True

	total_move_cnt += (M - 1)
	if too_small:
		total_move_cnt = min(3, total_move_cnt)
	print(total_move_cnt + 1)