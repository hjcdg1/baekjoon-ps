from sys import stdin
from itertools import combinations


N = int(stdin.readline())
TP = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = 0

# 시간 복잡도 : O(nC1 + nC2 + . . . + nCn) => O(2^n - 1) => O(2^n)
for i in range(1, N + 1):
	for combination in combinations(range(N), i):
		is_correct = True
		for idx, date in enumerate(combination):
			end_date = (date - 1) + TP[date][0]
			if end_date >= N:
				is_correct = False
				break
			elif idx + 1 < i and end_date >= combination[idx + 1]:
				is_correct = False
				break

		if not is_correct:
			continue

		answer = max(answer, sum([TP[date][1] for date in combination]))

print(answer)
