from sys import stdin


N = int(stdin.readline())
A = stdin.readline().split()
K = len(A)

# 최댓값 찾기

numbers_asc = list(range(10))
answer_max = ''

curr = 0
while curr < K:
	if A[curr] == '>':
		answer_max += str(numbers_asc.pop())
		curr += 1
	else:
		cnt = 0
		while curr < K and A[curr] == '<':
			cnt += 1
			curr += 1

		max_backup = numbers_asc.pop()
		answer_max += ''.join(map(str, reversed([numbers_asc.pop() for _ in range(cnt)])))
		numbers_asc.append(max_backup)

answer_max += str(numbers_asc.pop())
print(answer_max)

# 최솟값 찾기

numbers_desc = list(reversed(range(10)))
answer_min = ''

curr = 0
while curr < K:
	if A[curr] == '<':
		answer_min += str(numbers_desc.pop())
		curr += 1
	else:
		cnt = 0
		while curr < K and A[curr] == '>':
			cnt += 1
			curr += 1

		min_backup = numbers_desc.pop()
		answer_min += ''.join(map(str, reversed([numbers_desc.pop() for _ in range(cnt)])))
		numbers_desc.append(min_backup)

answer_min += str(numbers_desc.pop())
print(answer_min)
