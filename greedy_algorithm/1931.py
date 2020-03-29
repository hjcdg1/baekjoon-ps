N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]

M_sorted = sorted(M, key=lambda x: x[0])
M_sorted = sorted(M_sorted, key=lambda x: x[1])

last_finish_time = 0
result = 0
for m in M_sorted:
	if last_finish_time <= m[0]:
		result += 1
		last_finish_time = m[1]
print(result)