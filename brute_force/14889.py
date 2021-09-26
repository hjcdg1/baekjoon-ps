from sys import stdin
from itertools import combinations, permutations


N = int(stdin.readline())
S = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = float('inf')
for team1 in combinations(range(N), N // 2):
	team1_power = sum([S[i][j] for i, j in permutations(team1, 2)])

	team2 = set(range(N)) - set(team1)
	team2_power = sum([S[i][j] for i, j in permutations(team2, 2)])

	answer = min(answer, abs(team1_power - team2_power))

print(answer)
