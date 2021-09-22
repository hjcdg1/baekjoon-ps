from sys import stdin


N, M, K = list(map(int, stdin.readline().split()))

if not (M + K - 1 <= N <= M * K):
	print(-1)

else:
	groups = [[] for _ in range(M)]

	# 크기가 K인 첫 번째 그룹 구성
	groups[0].extend(list(range(1, K + 1)))

	# 나머지 (M - 1)개의 그룹 구성
	curr_group_idx = 1
	for n in range(K + 1, N + 1):
		groups[curr_group_idx].append(n)

		if curr_group_idx == M - 1:
			curr_group_idx = 1
		else:
			curr_group_idx += 1

	# 그룹 내 최댓값을 기준으로 그룹 순서 정렬
	groups.sort(key=lambda group: max(group))

	# 각 그룹 내 요소들의 순서를 내림차순으로 정렬
	for group in groups:
		group.sort(reverse=True)

	answer = ' '.join([' '.join(map(str, group)) for group in groups])
	print(answer)
