from sys import stdin


N, K = list(map(int, stdin.readline().split()))
E = list(map(int, stdin.readline().split()))

multitab = []
cnt = 0

for e_idx, e in enumerate(E):
	# 이미 꽂혀 있는 경우
	if e in multitab:
		continue

	# 빈 구멍 있음
	if len(multitab) < N:
		multitab.append(e)

	# 빈 구멍 없음
	else:
		remaining_E = E[e_idx + 1:]
		change_idx = -1
		max_occur_idx = -1

		for m_idx, m in enumerate(multitab):
			if m not in remaining_E:
				change_idx = m_idx
				break
			else:
				occur_idx = remaining_E.index(m)
				if occur_idx > max_occur_idx:
					max_occur_idx = occur_idx
					change_idx = m_idx

		multitab[change_idx] = e
		cnt += 1

print(cnt)
