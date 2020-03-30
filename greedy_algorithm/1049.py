import sys


N, M = tuple(map(int, sys.stdin.readline().split()))
P = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

p0_min = min([p[0] for p in P])
p1_min = min([p[1] for p in P])

if p0_min <= 6 * p1_min:
	option1 = p0_min * (N // 6) + p1_min * (N - 6 * (N // 6))
	option2 = p0_min * (N // 6 + 1)
	result = min(option1, option2)
else:
	result = p1_min * N

print(result)