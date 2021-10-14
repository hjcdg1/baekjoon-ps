from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N = int(stdin.readline())
	S = [0] + list(map(int, stdin.readline().split()))

	has_team = [None for _ in range(N + 1)]

	for v in range(1, N + 1):
		if has_team[v] is None:
			visit = set()
			path = []

			start = v
			while True:
				# start 방문
				visit.add(start)
				path.append(start)

				# start가 선택한 end
				end = S[start]

				# end가 방문된 적 있는 경우
				if end in visit:
					end_idx = path.index(end)
					for idx, i in enumerate(path):
						has_team[i] = True if idx >= end_idx else False
					break

				# end의 팀 소속 여부가 이미 결정된 경우
				elif has_team[end] is not None:
					for i in path:
						has_team[i] = False
					break

				start = end

	print(len([v for v in range(1, N + 1) if not has_team[v]]))
