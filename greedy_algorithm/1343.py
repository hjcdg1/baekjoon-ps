from sys import stdin


P = list(stdin.readline().rstrip())

P_len = len(P)
idx = 0

while idx < P_len:
	if P[idx] == 'X':
		start = idx
		end = (start + P[start:].index('.')) if '.' in P[start:] else P_len

		P_sub_len = end - start
		if P_sub_len % 2 == 1:
			print(-1)
			exit(0)

		AAAA_cnt = P_sub_len // 4
		BBBB_cnt = 1 if P_sub_len % 4 == 2 else 0

		P[start:start + 4 * AAAA_cnt] = ['A', 'A', 'A', 'A'] * AAAA_cnt
		if BBBB_cnt > 0:
			P[end - 2:end] = ['B', 'B']
		idx = end
	else:
		idx += 1

print(''.join(P))
