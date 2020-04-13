# Try again

import sys, heapq


N, K = tuple(map(int, sys.stdin.readline().split()))
MV = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
C = [int(sys.stdin.readline()) for _ in range(K)]

MV.sort(key=lambda x: x[0])
C.sort()

heap = []
idx = 0
result = 0
for c in C:
	while idx < len(MV) and MV[idx][0] <= c:
		heapq.heappush(heap, (-MV[idx][1], MV[idx][0]))
		idx += 1
	if heap:
		result += -heapq.heappop(heap)[0]
print(result)