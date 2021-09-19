from sys import stdin
import heapq


N, K = list(map(int, stdin.readline().split()))
MV = [list(map(int, stdin.readline().split())) for _ in range(N)]
C = [int(stdin.readline()) for _ in range(K)]

MV.sort(key=lambda x: x[0])  # 무게 기준 정렬
C.sort()  # 최대 무게 기준 정렬

heap = []
idx = 0
answer = 0

for c in C:
	while idx < len(MV) and MV[idx][0] <= c:
		heapq.heappush(heap, -MV[idx][1])
		idx += 1
	if heap:
		answer += -heapq.heappop(heap)

print(answer)
