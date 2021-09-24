from sys import stdin
from itertools import combinations


answer = []

while True:
	line = stdin.readline().split()
	if line[0] == '0':
		break

	answer.append(
		'\n'.join([' '.join(combination) for combination in combinations(line[1:], 6)])
	)

print('\n\n'.join(answer))
