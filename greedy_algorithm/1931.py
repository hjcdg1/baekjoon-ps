from sys import stdin


N = int(stdin.readline())
M = [list(map(int, stdin.readline().split())) for _ in range(N)]

M.sort(key=lambda x: x[0])
M.sort(key=lambda x: x[1])

last_finish_time = M[0][1]
answer = 1
for m in M[1:]:
	if m[0] < last_finish_time:
		continue
	answer += 1
	last_finish_time = m[1]

print(answer)
