# Tray again

import sys


T = int(sys.stdin.readline())
T_list = [{'N': 0, 'R': None} for _ in range(T)]
for t in range(T):
	T_list[t]['N'] = int(sys.stdin.readline())
	T_list[t]['R'] = [tuple(map(int, sys.stdin.readline().split())) for _ in range(T_list[t]['N'])]

for T_dict in T_list:
	N = T_dict['N']
	R = T_dict['R']

	R_sorted = sorted(R, key=lambda x: x[0])

	cnt = 1
	interview_rank = R_sorted[0][1]
	for r in R_sorted[1:]:
		if r[1] < interview_rank:
			cnt += 1
			interview_rank = r[1]
	print(cnt)