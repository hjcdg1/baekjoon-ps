from sys import stdin
from itertools import combinations


N, S = list(map(int, stdin.readline().split()))
A = list(map(int, stdin.readline().split()))

answer = 0
for i in range(1, N + 1):
	for combination in combinations(A, i):
		if sum(combination) == S:
			answer += 1

print(answer)
