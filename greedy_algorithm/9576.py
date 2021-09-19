from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N, M = list(map(int, stdin.readline().split()))
	AB = [list(map(int, stdin.readline().split())) for _ in range(M)]

	AB.sort(key=lambda x: x[0])  # 시작점 기준 정렬

	answer = 0
	for book in range(1, N + 1):
		# 더 이상 책을 할당해줄 수 있는 구간이 없음
		if not AB:
			break

		# 현재 책을 할당해줄 수 있는 구간이 없음
		if book < AB[0][0]:
			continue

		# 가장 범위가 좁은 구간에게 책을 할당
		idx = 0
		min_end_idx = None
		pop_idx = None
		for idx, ab in enumerate(AB):
			if book < ab[0]:
				break
			elif ab[1] < book:  # 할당할 수 없는 구간은 패스
				continue
			elif min_end_idx is None or ab[1] < min_end_idx:
				min_end_idx = ab[1]
				pop_idx = idx
		if pop_idx is not None:
			AB.pop(pop_idx)
			answer += 1

	print(answer)
