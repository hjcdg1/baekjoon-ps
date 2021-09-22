from sys import stdin


N, C = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
I = [list(map(int, stdin.readline().split())) for _ in range(M)]

# 도착지 기준으로 오름차순 정렬
I.sort(key=lambda x: x[1])

# load[i] : 마을 i에서 싣고 있는 택배의 양
load = [0 for _ in range(N + 1)]

answer = 0
for interval in I:
	max_load = 0
	for i in range(interval[0], interval[1]):
		max_load = max(max_load, load[i])

	amount = min(C - max_load, interval[2])
	if amount > 0:
		for i in range(interval[0], interval[1]):
			load[i] += amount
		answer += amount

print(answer)
