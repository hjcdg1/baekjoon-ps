from sys import stdin


N = int(stdin.readline())
K = int(stdin.readline())
S = list(map(int, stdin.readline().split()))

if K >= N:
	print(0)

else:
	S.sort()

	intervals = [{
		'start': S[idx],
		'end': S[idx + 1],
		'gap': S[idx + 1] - S[idx]
	} for idx in range(N - 1)]
	intervals.sort(key=lambda interval: interval['gap'])

	max_gaps = [intervals.pop()['gap'] for _ in range(K - 1)]

	print((S[-1] - S[0]) - sum(max_gaps))
