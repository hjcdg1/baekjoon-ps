# Failed

from sys import stdin


N, C = tuple(map(int, stdin.readline().split()))
M = int(stdin.readline())
D = [[] for _ in range(N + 1)]
for _ in range(M):
	start, end, number = tuple(map(int, stdin.readline().split()))
	D[start].append((end, number))

current_amount = 0
current = [0 for _ in range(N + 1)]
result = 0

for n in range(1, N + 1):
	# 내림
	if current[n] > 0:
		amount = current[n]
		current[n] = 0
		current_amount -= amount
		result += amount

	# 실음
	D[n].sort(key=lambda x: x[0])
	for d in D[n]:
		if current_amount == C:
			break
		amount = min(C - current_amount, d[1])
		current[d[0]] += amount
		current_amount += amount

print(result)