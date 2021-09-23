from sys import stdin
from itertools import combinations


H = [int(stdin.readline()) for _ in range(9)]

for combination in combinations(H, 7):
	if sum(combination) == 100:
		for h in sorted(list(combination)):
			print(h)
		break
