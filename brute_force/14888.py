from sys import stdin
from itertools import permutations


def calculate(x, y, op):
	if op == '+':
		return x + y
	elif op == '-':
		return x - y
	elif op == '*':
		return x * y
	else:
		return x // y if x >= 0 else -(-x // y)

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
add_cnt, sub_cnt, mul_cnt, div_cnt = list(map(int, stdin.readline().split()))

combinations = set(permutations('+' * add_cnt + '-' * sub_cnt + '*' * mul_cnt + '/' * div_cnt, N - 1))
answer_max = float('-inf')
answer_min = float('inf')

for combination in combinations:
	result = A[0]
	for i in range(N - 1):
		result = calculate(result, A[i + 1], combination[i])
	answer_max = max(answer_max, result)
	answer_min = min(answer_min, result)

print(answer_max)
print(answer_min)
