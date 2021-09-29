from sys import stdin
from itertools import combinations_with_replacement


T = int(stdin.readline())
K = [int(stdin.readline()) for _ in range(T)]

# 삼각수의 목록
max_K = max(K)
tri_numbers = []
n = 1
while True:
	tri_number = (n * (n + 1)) / 2
	if tri_number >= max_K:
		break
	tri_numbers.append(tri_number)
	n += 1

# 삼각수 3개를 이용하여 만들 수 있는 값의 목록
possible_numbers = [
	sum(combination)
	for combination in combinations_with_replacement(tri_numbers, 3)
]

for k in K:
	print(1 if k in possible_numbers else 0)
