# Try again

import sys


N, K = tuple(map(int, sys.stdin.readline().split()))
E = list(map(int, sys.stdin.readline().split()))

pos = [[] for _ in range(K + 1)]
for i in range(K - 1, -1, -1):
	pos[E[i]].append(i)

cnt = 0
plugged_in = set()

for e in E:
	pos[e].pop()

	if e in plugged_in:
		continue
	else:
		if len(plugged_in) == N:
			max_p = None
			for p in plugged_in:
				if not pos[p]:
					max_p = p
					break
				elif max_p is None:
					max_p = p
				elif pos[p][-1] > pos[max_p][-1]:
					max_p = p
			plugged_in.remove(max_p)
			cnt += 1
		plugged_in.add(e)

print(cnt)