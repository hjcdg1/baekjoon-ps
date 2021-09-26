from sys import stdin
from itertools import combinations


N, M = list(map(int, stdin.readline().split()))
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

houses = []
chicken_houses = []
for i in range(N):
	for j in range(N):
		if A[i][j] == 1:
			houses.append((i, j))
		elif A[i][j] == 2:
			chicken_houses.append((i, j))

answer = float('inf')
for combination in combinations(chicken_houses, M):
	city_chicken_d = 0
	for house_i, house_j in houses:
		chicken_d = float('inf')
		for chicken_house_i, chicken_house_j in combination:
			chicken_d = min(
				chicken_d,
				abs(house_i - chicken_house_i) + abs(house_j - chicken_house_j)
			)
		city_chicken_d += chicken_d
	answer = min(answer, city_chicken_d)

print(answer)
