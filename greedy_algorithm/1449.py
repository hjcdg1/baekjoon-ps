import sys

N, L = tuple(map(int, sys.stdin.readline().split()))
P = sorted(list(map(int, sys.stdin.readline().split())))

cnt = 0
start, end = 0, 0
for p in P:
	if p + 0.5 <= end:
		continue
	else:
		start = p - 0.5
		end = start + L
		cnt += 1
print(cnt)