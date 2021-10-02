from sys import stdin


def get_divisors(number):
	divisors = set()
	for divisor in range(1, int(number ** (1/2)) + 1):
		if number % divisor == 0:
			divisors.add(divisor)
			divisors.add(number // divisor)
	return list(sorted(list(divisors)))[1:]  # 1은 제외

N = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(N)]

# 오름차순 정렬
numbers.sort()

# 두 번째 값부터, numbers[0]를 뺀 결과의 약수들을 조사하면 된다.
numbers = numbers[:1] + [number - numbers[0] for number in numbers[1:]]
candidates = get_divisors(numbers[1])
for number in numbers[2:]:
	new_candidates = set()
	for candidate in candidates:
		if number % candidate == 0:
			new_candidates.add(candidate)
	candidates = new_candidates

print(' '.join(map(str, sorted(candidates))))
