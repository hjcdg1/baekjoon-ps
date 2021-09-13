from sys import stdin 


T = int(stdin.readline())
for _ in range(T):
	N = int(stdin.readline())
	R = [list(map(int, stdin.readline().split())) for _ in range(N)]

	R.sort(key=lambda r: r[0])

	answer = 1
	min_r = R[0][1]
	for r in R[1:]:
		if r[1] < min_r:
			answer += 1
		min_r = min(min_r, r[1])

	print(answer)
