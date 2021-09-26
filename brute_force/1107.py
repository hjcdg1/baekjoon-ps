from sys import stdin
from itertools import product


N = int(stdin.readline())
M = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

N_len = len(str(N))
numbers = [number for number in range(10) if number not in B]

answer = abs(N - 100)

if not numbers:
	print(answer)

else:
	# 자릿수가 같은 숫자들 탐색
	for permutation in product(numbers, repeat=N_len):
		number = int(''.join(map(str, permutation)))
		answer = min(answer, len(str(number)) + abs(N - number))

	# 자릿수가 하나 더 많은 숫자들(1로 시작) 탐색
	if 1 in numbers:
		for permutation in product(numbers, repeat=N_len):
			number = int('1' + ''.join(map(str, permutation)))
			answer = min(answer, len(str(number)) + abs(N - number))

	# 자릿수가 하나 더 적은 숫자들 탐색
	if N_len > 1:
		for permutation in product(numbers, repeat=N_len - 1):
			number = int(''.join(map(str, permutation)))
			answer = min(answer, len(str(number)) + abs(N - number))

	print(answer)
