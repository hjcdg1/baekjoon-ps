from sys import stdin
from itertools import permutations


def compare(candidate, number):
	candidate = str(candidate)
	number = str(number)

	strike, ball = 0, 0
	for i in range(3):
		if candidate[i] == number[i]:
			strike += 1
		elif number[i] in candidate:
			ball += 1

	return strike, ball

def filter_candidates(candidates, number, strike, ball):
	new_candidates = set()
	for candidate in candidates:
		if compare(candidate, number) == (strike, ball):
			new_candidates.add(candidate)
	return new_candidates

N = int(stdin.readline())
Q = [list(map(int, stdin.readline().split())) for _ in range(N)]

candidates = set([
	int(''.join(map(str, permutation)))
	for permutation in permutations(range(1, 10), 3)
])

for number, strike, ball in Q:
	candidates = filter_candidates(candidates, number, strike, ball)

print(len(candidates))
